
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

"""--- Main handler --- """

def lambda_handler(event, context):

# 	os.environ['TZ'] = 'America/New_York'
# 	time.tzset()
# 	logger.debug('event.bot.name={}'.format(event['bot']['name']))

	return dispatch(event)

def dispatch(intent_request):

	intent_name = intent_request['currentIntent']['name']

	#Dispatch to bot's intent handlers
	if intent_name == 'sayHello': #++++++++++++++
		return get_info(intent_request)
	raise Exception('Intent with name' + intent_name + ' not supported')

def get_info(intent_request): 
	return {"dialogAction": {
		"type": "Close",
		"fulfillmentState": "Fulfilled",
		"message": {
			"contentType": "PlainText",
			"content": "hello!"
		}
	}}