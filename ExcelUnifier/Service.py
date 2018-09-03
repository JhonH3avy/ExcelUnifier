import arrow

class Service(object):
    """Flight object to be inserted in database"""
    def __init__(self, fields = []):
        if 'date' in fields.keys() and fields['date']:
            self.date = fields['date']
        else:
            self.date = None
        if 'airline' in fields.keys() and fields['airline']:
            self.airline = fields['airline']
        else:
            self.airline = 'AVIANCA'
        if 'flight_number' in fields.keys() and fields['flight_number']:
            self.flight_number = fields['flight_number']
        else:
            self.flight_number = None
        if 'origin' in fields.keys() and fields['origin']:
            self.origin = fields['origin']
        else:
            self.origin = None
        if 'destination' in fields.keys() and fields['destination']:
            self.destination = fields['destination']
        else:
            self.destination = None
        if 'pax_name' in fields.keys() and fields['pax_name']:
            self.pax_name = fields['pax_name']
        else:
            self.pax_name = None
        if 'service_terminal' in fields.keys() and fields['service_terminal']:
            self.service_terminal = fields['service_terminal']
        else:
            self.service_terminal = None        
        if 'WCOB' in fields.keys() and fields['WCOB']:
            self.wcob = fields['WCOB']
        else:
            self.wcob = None
        if 'WCMP' in fields.keys() and fields['WCMP']:
            self.wcmp = fields['WCMP']
        else:
            self.wcmp = None
        if 'WCHS' in fields.keys() and fields['WCHS']:
            self.wchs = fields['WCHS']
        else:
            self.wchs = None
        if 'WCHR' in fields.keys() and fields['WCHR']:
            self.wchr = fields['WCHR'] 
        else:
            self.wchr = None
        if 'WCHC' in fields.keys() and fields['WCHC']:
            self.wchc = fields['WCHC']
        else:
            self.wchc = None
        if 'WCBW' in fields.keys() and fields['WCBW']:
            self.wcbw =  fields['WCBW']
        else:
            self.wcbw = None


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



