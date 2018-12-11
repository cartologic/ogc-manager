from uuid import uuid4

from geonode.people.models import Profile

from .constants import SLUGIFIER
from .exceptions import ConfigurationException


class LayerConfig(object):
    def __init__(self, config={}):
        if not isinstance(config, dict):
            raise ConfigurationException("config_dict should be dict")
        self.config_dict = config
        self.name = self.config_dict.get('name', None)
        self.permissions = self.config_dict.get('permissions', None)
        self.overwrite = self.config_dict.get('overwrite', False)
        self.temporary = self.config_dict.get('temporary', False)
        self.launder = self.config_dict.get('launder', False)
        self.username = self.config_dict.get('username', False)

    def get_user(self):
        if not self.username:
            user_query = Profile.objects.filter(is_superuser=True)
            if user_query.count():
                user = user_query.first()
            else:
                pass
            self.username = user.username
        else:
            user = Profile.objects.get(username=self.username)
        return user

    def _unique_name(self):
        from .layers import OSGEOLayer
        if len(self.name) > 63:
            self.name = self.name[:63]
        if not OSGEOLayer.check_geonode_layer(self.name):
            return str(self.name)
        suffix = uuid4().__str__().split('-').pop()
        if len(self.name) < (63 - (len(suffix) + 1)):
            self.name += "_" + suffix
        else:
            self.name = self.name[:((63 - len(suffix)) - 2)] + "_" + suffix

        return self._unique_name()

    def get_new_name(self):
        self.name = SLUGIFIER(self.name.lower())
        if not self.overwrite:
            return self._unique_name()
        return self.name

    def as_dict(self):
        d = vars(self)
        d.pop('config_dict', None)
        return d
