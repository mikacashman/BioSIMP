# -*- coding: utf-8 -*-
#BEGIN_HEADER
#END_HEADER


class BioSIMP:
    '''
    Module Name:
    BioSIMP

    Module Description:
    A KBase module: BioSIMP
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        #END_CONSTRUCTOR
        pass


    def BioSIMP(self, ctx, params):
        """
        :param params: instance of type "BioSIMPParams" (Insert your typespec
           information here.) -> structure: parameter "workspace_name" of
           String, parameter "fbamodel_id" of String, parameter "media" of
           String, parameter "fbaOuptut_id" of String
        :returns: instance of type "BioSIMPOutput" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN BioSIMP
	### STEP 1 - Parse input and catch any errors
	if 'workspace_name' not in params:
		raise ValueError('Parameter workspace is not set in input arguments')
	workspace_name=params['workspace_name']
	if 'fbamodel_id' not in params:
		raise ValueError('Parameter FBAModel is not set in input arguments')
	if 'media' not in params:
		raise ValueError('Parameter Media is not set in input arguments')
	if 'fbaOutput_id' not in params:
		raise ValueError('Parameter FBA output ID is not set in input arguments')

	### STEP 2 - Get the Input Data
	token = ctx['token']
	wsClient = workspaceServices(self.workspaceURL, token=token)
	try:
		fbamodel = wsClient.get_objects([{'ref':params['fbamodel_id']}])[0]['data']
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
		orig_error = ''.join('   ' + line for line in lines)
		raise ValueError('Error loading FBAModel object from workspace:\n' + orig_error)
	print('Got FBAModel')
	try:
		media = wsClient.get_objects([{'ref':params['media']}])[0]['data']
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
		orig_error = ''.join('   ' + line for line in lines)
		raise ValueError('Error loading Media object from workspace:\n' + orig_error)
	print('Got Media')


	

        #END BioSIMP

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method BioSIMP return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
