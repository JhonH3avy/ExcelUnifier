import arrow

class Service(object):
    """Flight object to be inserted in database"""
    def __init__(self, fields = []):
        self.date = None
        self.airline = 'AVIANCA'
        self.flight_number = None
        self.origin = None
        self.destination = None
        self.pax_name = None
        self.service_terminal = None 
        self.wcob = None
        self.wcmp = None
        self.wchs = None
        self.wchr = None
        self.wchc = None
        self.wcbw = None

        if 'date' in fields.keys() and fields['date']:
            self.date = fields['date']
        if 'airline' in fields.keys() and fields['airline']:
            self.airline = fields['airline']
        if 'flight_number' in fields.keys() and fields['flight_number']:
            self.flight_number = fields['flight_number']
        if 'origin' in fields.keys() and fields['origin']:
            self.origin = fields['origin']
        if 'destination' in fields.keys() and fields['destination']:
            self.destination = fields['destination']
        if 'pax_name' in fields.keys() and fields['pax_name']:
            self.pax_name = fields['pax_name']
        if 'service_terminal' in fields.keys() and fields['service_terminal']:
            self.service_terminal = fields['service_terminal']      
        if 'WCOB' in fields.keys() and fields['WCOB']:
            self.wcob = fields['WCOB']
        if 'WCMP' in fields.keys() and fields['WCMP']:
            self.wcmp = fields['WCMP']
        if 'WCHS' in fields.keys() and fields['WCHS']:
            self.wchs = fields['WCHS']
        if 'WCHR' in fields.keys() and fields['WCHR']:
            self.wchr = fields['WCHR']
        if 'WCHC' in fields.keys() and fields['WCHC']:
            self.wchc = fields['WCHC']
        if 'WCBW' in fields.keys() and fields['WCBW']:
            self.wcbw =  fields['WCBW']


    def is_valid_service(self):
        if not self.date:
            return False
        if not self.flight_number:
            return False
        if not self.airline:
            return False
        if not self.pax_name:
            return False
        if not self.service_terminal:
            return False
        if not self.origin:
            return False
        if not self.destination:
            return False
        return True


    def is_arriving(self, reference):
        return self.destination == reference



