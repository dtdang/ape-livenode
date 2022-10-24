from ape.api import ProviderAPI

class LiveNodeProvider(ProviderAPI):
    _is_conncted: bool = False
    
    def connect(self):
        self._is_conncted = True
        
    @property
    def chain_id(self) -> int:
        return 50
    
    def disconnect(self):
        pass
    def estimate_gas_cost(self):
        pass
    @property
    def gas_price(self):
        pass
    def get_balance(self):
        pass
    def get_block(self):
        pass
    def get_code(self):
        pass
    def get_contract_logs(self):
        pass
    def get_nonce(self):
        pass
    def get_receipt(self):
        pass
    def get_transactions_by_block(self):
        pass
    def send_call(self):
        pass
    def send_transaction(self):
        pass
    def update_settings(self):
        pass
    @property
    def is_connected(self):
        pass