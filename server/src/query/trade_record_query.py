from ..database.trade_record import TradeRecord, TradeRecordCreate, TradeRecordUpdate
from .base_query import BaseQuery


class TradeRecordQuery(BaseQuery[TradeRecord, TradeRecordCreate, TradeRecordUpdate]):
    ...


trade_record = TradeRecordQuery(TradeRecord)
