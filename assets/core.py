#coding:utf8
__author__ = 'liuhui'

import json
from django.core.exceptions import ObjectDoesNotExist
from assets.models import Host
from accounts.models import UserProfile

class Asset():

    def __init__(self, request):
        self.request = request
        self.mandatory_fields = ['sn', 'asset_id']
        self.response = {
            'error': [],
            'info': [],
            'warning': [],
        }

    def response_msg(self, msg_type, key, msg):
        if msg_type in self.response:
            self.response[msg_type].append({key: msg})
        else:
            raise ValueError

    def mandatory_check(self, data, only_check_sn=False):
        for field in self.mandatory_fields:
            if field not in data:
                self.response_msg('error', 'MandatoryCheckFailed',
                                  "The field [{}] is mandatory and not provided in your reporting data".format(field))
        else:
            if self.response['error']:
                return False
        try:
            if not only_check_sn:
                self.asset_obj = Host.objects.get(id=int(data['asset_id']), sn=data['sn'])
            else:
                self.asset_obj = Host.objects.get(sn=data['sn'])
            return True
        except ObjectDoesNotExist as e:
            print(e)
            self.response_msg('error', 'AssetDataInvalid',
                              "Cannot find asset object in DB by using asset id [{}] and SN [{}]".format(data['asset_id'], data['sn']))
            self.waiting_approval = True
            return False

    def get_asset_id_by_sn(self):
        data = self.request.POST.get('asset_info')
        response = {}
        if data:
            try:
                data = json.loads(data)
                if self.mandatory_check(data, only_check_sn=True):
                    response = {'asset_id': self.asset_obj.id}
                else:
                    if hasattr(self, 'waiting_approval'):
                        response = {'needs_approval': "this is a new asset,needs IT admin's approval to create the new asset id."}
                        self.clean_data = data
                        self.data_inject()
                        print(response)
                    else:
                        response = self.response
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
                response = self.response
        return response

    def data_is_valid(self):
        data = self.request.POST.get('asset_info')
        if data:
            try:
                data = json.loads(data)
                self.mandatory_check(data)
                self.clean_data = data
                if not self.response['error']:
                    return True
            except ValueError as e:
                self.response_msg('error', 'AssetDataInvalid', str(e))
        else:
            self.response_msg('error', 'AssetDataInvalid',
                              "The reported asset data is not valid or provided")

    def __is_new_asset(self):
        if not self.clean_data.get('asset_id'):
            return True
        else:
            return False

    def data_inject(self):
        if self.__is_new_asset():
            print('\033[32;1m---new asset,going to create----\033[0m')
            self.create_asset()
        else:
            #print('\033[33;1m---asset already exist ,going to update----\033[0m')
            self.update_asset_component()


    def create_asset(self, ignore_errs=False):
        data = self.request.POST.get('asset_info')
        if data:
            try:
                data = json.loads(data)
                data_set = {
                    'hostname': self.clean_data.get('hostname'),
                    'ipaddress': self.clean_data.get('ipaddress'),
                    'macaddress': self.clean_data.get('macaddress'),
                    'os_type': self.clean_data.get('os_type'),
                    'os_version': self.clean_data.get('os_version'),
                    'Manufactory': self.clean_data.get('Manufactory'),
                    'sn': self.clean_data.get('sn'),
                    'cpu_model': self.clean_data.get('cpu_model'),
                    'cpu_num': self.clean_data.get('cpu_num'),
                    'cpu_physical': self.clean_data.get('cpu_physical'),
                    'memory': self.clean_data.get('memory'),
                    'disk': self.clean_data.get('disk'),
                }
                host = Host(**data_set)
                host.save()
                asset_obj = Host.objects.get(sn=self.clean_data.get('sn'))
                data['asset_id'] = asset_obj.id
                self.mandatory_check(data)
                self.clean_data = data
                if not self.response['error']:
                    return True
            except Exception as e:
                self.response_msg('error', 'ObjectCreationException', 'Object [server] {}'.format(str(e)))


    def update_asset_component(self):
        update_fields = ['hostname','ipaddress','os_type','os_version','cpu_model','cpu_num','cpu_physical','memory','disk']
        self.compare_componet(asset_obj=self.asset_obj,
                              field_from_db=update_fields,
                              data_source=self.clean_data,
                              )

    def compare_componet(self, asset_obj, field_from_db, data_source):
        #print('--going to compare:[{}]'.format(asset_obj),field_from_db)
        #print('--source data:', data_source)
        for field in field_from_db:
            var_from_db = getattr(asset_obj, field)
            var_from_data_source = data_source.get(field)
            if var_from_data_source:
                if type(var_from_db) in (int,):
                    var_from_data_source = int(var_from_data_source)
                elif type(var_from_db) is float:
                    var_from_data_source = float(var_from_data_source)
                elif type(var_from_db) is str:
                    var_from_data_source = str(var_from_data_source)
                if var_from_db == var_from_data_source:
                    pass
                else:
                    print('\033[34;1m val_from_db[{}]  != val_from_data_source[{}]\033[0m'.format(
                        var_from_db, var_from_data_source), type(var_from_db), type(var_from_data_source), field)
                    db_field = asset_obj._meta.get_field(field)
                    db_field.save_form_data(asset_obj,var_from_data_source)
                    asset_obj.save()
                    log_msg = "Asset[{}] --> component[{}] --> field[{}] has changed from [{}] to [{}]".format(
                        self.asset_obj, asset_obj, field, var_from_db, var_from_data_source)
                    self.response_msg('info', 'FieldChanged', log_msg)
            else:
                self.response_msg('warning', 'AssetUpdateWarning',
                                  "Asset component [{}]'s field [{}] is not provided in reporting data ".format(
                                      asset_obj, field))
        asset_obj.save()


