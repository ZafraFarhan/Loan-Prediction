import streamlit as st
from PIL import Image
import pickle

# Load the RandomForestClassifier model from the pickle file
pickle_file_path = './loan_pred_model.pkl'

with open(pickle_file_path, 'rb') as f:
    model = pickle.load(f)

def run():
    #st.markdown("<h1 style='text-align: center; font-size: 80px; font-family: Comic Sans MS;'>FinLoan</h1>", unsafe_allow_html=True)
    #st.markdown("<h2 style='text-align: center; font-size: 15px; font-family: Suez One; font-weight: bold;'>Empowering Your Financial Journey</h2>", unsafe_allow_html=True)

    html_code = '''
    <figure class="image image_resized" style="width:38.38%;" data-ckbox-resource-id="pExlLCMgCXOw">
        <picture>
            <source srcset="https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/80.webp 80w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/160.webp 160w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/240.webp 240w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/320.webp 320w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/400.webp 400w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/480.webp 480w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/560.webp 560w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/640.webp 640w,https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/647.webp 647w" sizes="(max-width: 647px) 100vw, 647px" type="image/webp"><img src="https://ckbox.cloud/509c9c1f11e549c80adc/assets/pExlLCMgCXOw/images/647.png" width="647" height="161">
        </picture>
    </figure>
    '''
    st.markdown(html_code, unsafe_allow_html=True)

    
    navigation_links = {
    "Home": "https://aashafathima1.wixsite.com/finloan",
    "About Us": "https://aashafathima1.wixsite.com/finloan/about-us",
    "Approval Loan": "https://loan-prediction-cctzcfxv4nafgqyegjwgsb.streamlit.app/#finloan",
    "Request": "https://aashafathima1.wixsite.com/finloan/copy-of-about-us"
    }

    # Get the current page from URL
    current_page = st.experimental_get_query_params().get('page', 'Home')

    # Display horizontal tabs
    with st.sidebar:
        st.write("# Navigation")
        selected_page = st.radio("", list(navigation_links.keys()), index=list(navigation_links.keys()).index(current_page))
    



    # User inputs
    fn = st.text_input("First Name")

    loan_amt_str = st.text_input("Loan Amount ($)",value='')
    loan_amt = int(loan_amt_str) if loan_amt_str else None


    loanType_display = ('Personal Loan','Business Loan','House Loan','Debt Consolidation','Other')  
    loanType_options = list(range(len(loanType_display)))
    loanType = st.selectbox("Loan Purpose", loanType_options, format_func=lambda x: loanType_display[x])

    term_display = ('Short Term','Long Term')
    term_options = list(range(len(term_display)))
    term = st.selectbox("Term", term_options, format_func=lambda x: term_display[x])

    crdt_scr_str = st.text_input('Credit Score',value='')
    crdt_scr = int(crdt_scr_str) if crdt_scr_str else None

    annual_incm_str = st.text_input('Annual Income ($)',value='')
    annual_incm = int(annual_incm_str) if annual_incm_str else None

    exprnc_display = ('<3 years','3-6 years','7-9 years','10+ years')
    exprnc_options = list(range(len(exprnc_display)))
    exprnc = st.selectbox("Years of Experience", exprnc_options, format_func=lambda x: exprnc_display[x])

    home_display = ('Home Mortgage','Rent','Own Home','Have Mortgage')
    home_options = list(range(len(home_display)))
    home = st.selectbox("Home Ownership",  home_options, format_func=lambda x: home_display[x])

    debt_str = st.text_input('Monthly Debt',value='')
    debt = int(debt_str) if debt_str else None

    crdt_years_str = st.text_input('Years of Credit History',value='')
    crdt_years = int(crdt_years_str) if crdt_years_str else None

    opnAcc = st.number_input('No. of Open Accounts', value=0)

    crdtPrb = st.number_input('No. of Credit Problems', value=0)

    crdtBal_str = st.text_input('Current Credit Balance',value='')
    crdtBal = int(crdtBal_str) if crdtBal_str else None

    maxOpenCredt_str = st.text_input('Max Open Credit',value='')
    maxOpenCredt = int(maxOpenCredt_str) if maxOpenCredt_str else None

    bankruptcy = st.number_input('Bankruptcies', value=0)

    taxLien = st.number_input('Tax Liens', value=0)
    
    
    if st.button("Submit"):
        features = [[loan_amt, loanType, term, crdt_scr, annual_incm, exprnc, home, debt, crdt_years, opnAcc, crdtPrb, crdtBal, maxOpenCredt, bankruptcy, taxLien]]
        prediction = model.predict(features)
        
        if prediction == 0:
            st.error(
                "Hello: " + fn + " || "
                "According to our calculations, you will not get the loan from the bank."
            )
        else:
            st.success(
                "Hello: " + fn + " || "
                "Congratulations!! You will get the loan from the bank."
            )

run()
