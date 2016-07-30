from novaclient import base
from oslo_log import log as logging
LOG = logging.getLogger(__name__)
class Policys(base.Resource):
    def __repr__(self):
        return "<Policy: %s>" % self.id

    def delete(self):
        self.manager.delete(self)

class PolicysManager(base.ManagerWithFind):
    resource_class = Policys

    def list(self):
        LOG.info("v2_policy")
        return self._list('/os-policys','policys')
