from json import dumps
from oauthlib.common import urldecode


def facebook_compliance_fix(session):

    def _compliance_fix(r):
        token = dict(urldecode(r.text))
        token['expires_in'] = token['expires']
        token['token_type'] = 'Bearer'
        r._content = dumps(token)
        return r

    session.register_compliance_hook('access_token_response', _compliance_fix)
    return session
