# CONSTANTS
BASE_URL = "http://automationpractice.com/"
SEARCH_TERM = "dress"
VALID_EMAIL = "test@email.com"
TEST = "test"


# SELECTORS

# Home page
SEARCH_INPUT_FIELD = "#search_query_top"
CONTACTUS_BTN = "#contact-link > a"
TSHIRTS_CATEGORY = "#block_top_menu > ul > li:nth-child(3) > a"

# Search results page
SEARCH_HEADING = "h1.page-heading.product-listing"
SEARCH_RESULTS_ARRAY = "div.right-block h5 a.product-name"

# "Contact us" page
FORM = "form.contact-form-box"
FORM_SUBMIT_MESSAGE_BTN = "button#submitMessage"
FORM_SUBJECT_DROPDOWN = "select#id_contact"
FORM_EMAIL = "input#email"
FORM_ORDER_REFERENCE = "input#id_order"
FORM_ATTACHMENT = "input#fileUpload"
FORM_MESSAGE = "textarea#message"
ERROR_ALERT = "div.alert.alert-danger"

# T-shirts category page
PRODUCT_LIST = "#center_column > ul"
PRODUCT_FROM_FIRST_COLUMN = "li.first-in-line.last-line div.right-block h5 a"

# Product page
PRODUCT_DESCRIPTION = "#center_column > div > div"
ADD_TO_CART = "#add_to_cart > button > span"
PRODUCT_ADDED_CONFIRMATION_DIALOG = "#layer_cart > div.clearfix"
PRODUCT_ADDED_CONFIRMATION_BTN_CONTINUE = "div.button-container > span"
