from json import dumps, loads

def salesforce_compliance_fix(session):

    def _compliance_fix(r):
        token = dict(loads(r.text))
        token['token_type'] = 'Bearer'
        
        r._content = bytes(dumps(token), 'UTF-8')
        return r

    session.register_compliance_hook('access_token_response', _compliance_fix)
    return session
