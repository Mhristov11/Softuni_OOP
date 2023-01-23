class TicketPriceValidator:
    @staticmethod
    def validate(ticket_price):
        if ticket_price < 1.00:
            raise ValueError("Ticket price must be at least 1.00$!")
        return ticket_price
