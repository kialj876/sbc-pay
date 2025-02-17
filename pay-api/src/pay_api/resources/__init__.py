# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Exposes all of the resource endpoints mounted in Flask-Blueprint style.

Uses restplus namespaces to mount individual api endpoints into the service.

All services have 2 defaults sets of endpoints:
 - ops
 - meta
That are used to expose operational health information about the service, and meta information.
"""
from flask import Blueprint
from sbc_common_components.exception_handling.exception_handler import ExceptionHandler

from .account import API as ACCOUNTS_API
from .account_statements import API as ACCOUNT_STATEMENTS_API
from .account_statements_notifications import API as ACCOUNT_STATEMENT_NOTIFICATIONS_API
from .account_statements_settings import API as ACCOUNT_STATEMENTS_SETTINGS_API
from .apihelper import Api
from .bank_accounts import API as BANK_ACCOUNTS_API
from .code import API as CODES_API
from .distributions import API as DISTRIBUTION_API
from .fas import ROUTING_SLIP_API, ROUTING_SLIP_REFUND_API
from .fee import API as FEE_API
from .fee_schedule import API as FEE_SCHEDULE_API
from .invoice import API as INVOICE_API
from .invoice_receipt import API as INVOICE_RECEIPT_API
from .invoices import API as INVOICES_API
from .meta import API as META_API
from .ops import API as OPS_API
from .payment import API as PAYMENT_API
from .refund import API as REFUND_API
from .transaction import API as TRANSACTION_API


__all__ = ('API_BLUEPRINT', 'OPS_BLUEPRINT')

# This will add the Authorize button to the swagger docs
# TODO oauth2 & openid may not yet be supported by restplus <- check on this
AUTHORIZATIONS = {'apikey': {'type': 'apiKey', 'in': 'header', 'name': 'Authorization'}}

OPS_BLUEPRINT = Blueprint('API_OPS', __name__, url_prefix='/ops')

API_OPS = Api(
    OPS_BLUEPRINT,
    title='Service OPS API',
    version='1.0',
    description='The Core API for the Payment System',
    security=['apikey'],
    authorizations=AUTHORIZATIONS,
)

API_OPS.add_namespace(OPS_API, path='/')

API_BLUEPRINT = Blueprint('API', __name__, url_prefix='/api/v1')

API = Api(
    API_BLUEPRINT,
    title='Payment API',
    version='1.0',
    description='The Core API for the Payment System',
    security=['apikey'],
    authorizations=AUTHORIZATIONS,
)

HANDLER = ExceptionHandler(API)

API.add_namespace(META_API, path='/meta')
API.add_namespace(INVOICE_API, path='/payment-requests')
API.add_namespace(FEE_API, path='/fees')
API.add_namespace(FEE_SCHEDULE_API, '/fees/schedules')
API.add_namespace(DISTRIBUTION_API, '/fees/distributions')
API.add_namespace(TRANSACTION_API, path='')
API.add_namespace(INVOICE_RECEIPT_API, path='/payment-requests/<int:invoice_id>')
API.add_namespace(INVOICES_API, path='/payment-requests/<int:invoice_id>/invoices')
API.add_namespace(ACCOUNTS_API, path='/accounts')
API.add_namespace(ACCOUNT_STATEMENTS_API, path='/accounts/<string:account_id>/statements')
API.add_namespace(ACCOUNT_STATEMENTS_SETTINGS_API, path='/accounts/<string:account_id>/statements/settings')
API.add_namespace(ACCOUNT_STATEMENT_NOTIFICATIONS_API, path='/accounts/<string:account_id>/statements/notifications')
API.add_namespace(BANK_ACCOUNTS_API, path='/bank-accounts/verifications')
API.add_namespace(REFUND_API, path='/payment-requests/<int:invoice_id>')
API.add_namespace(PAYMENT_API, path='/accounts/<string:account_id>/payments')

API.add_namespace(CODES_API, path='/codes')
API.add_namespace(ROUTING_SLIP_API, path='/fas/routing-slips')
API.add_namespace(ROUTING_SLIP_REFUND_API, path='/fas/routing-slips/<string:routing_slip_number>/refunds')
