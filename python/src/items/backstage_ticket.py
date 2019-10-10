from src.items.regular_item import RegularItem


class BackstageTicket(RegularItem):

    def _update_backstageticket_quality(self, backstage_ticket):
        """
        Helper function to update the backstage tickets their quality.
        :param backstage_ticket: item.
        :return: updated quality
        """
        if self._item_has_expired(backstage_ticket):
            return 0
        elif backstage_ticket.sell_in < 11:
            return self._increase_quality(backstage_ticket)
        else:
            return backstage_ticket.quality

    def update(self, backstage_ticket):
        """
        Helper funciton to update the backstage ticket.
        :param backstage_ticket: input item (backstage ticket)
        :return: updated ticket.
        """
        backstage_ticket.quality = self._increase_quality(backstage_ticket)
        backstage_ticket.quality = self._update_backstageticket_quality(backstage_ticket)
        backstage_ticket.sell_in = backstage_ticket.sell_in - 1
        if backstage_ticket.sell_in < 0:
            backstage_ticket.quality = self._update_backstageticket_quality(backstage_ticket)
            return backstage_ticket
        else:
            return backstage_ticket