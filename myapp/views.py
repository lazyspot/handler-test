import logging
from pyramid.view import view_config
from pyramid.response import Response

log = logging.getLogger(__name__)

@view_config(route_name='home')
def root(request):
    log.debug('exception impending!')
    try:
        1/0
    except:
        log.exception('1/0 error')
    log.info('test complete')
    return Response("test complete!")