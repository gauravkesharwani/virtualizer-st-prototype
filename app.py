import streamlit as st 


from streamlit_lottie import st_lottie
import requests
from PIL import Image
from streamlit_option_menu import option_menu
import webbrowser


if 'current_view' not in st.session_state:
    st.session_state['current_view'] = 'Grid'

if 'current_step' not in st.session_state:
    st.session_state['current_step'] = 1

if 'queued_file' not in st.session_state:
    st.session_state['queued_file'] = 1

def set_page_view(page):
    st.session_state['current_step'] = 1 
    st.session_state['queued_file'] = None
    st.session_state['current_view'] = page      

def set_form_step(action,step=None):
    if action == 'Next':
        st.session_state['current_step'] = st.session_state['current_step'] + 1
    if action == 'Back':
        st.session_state['current_step'] = st.session_state['current_step'] - 1
    if action == 'Jump':
        st.session_state['current_step'] = step

##### wizard functions ####
# def wizard_form_header():
   
             
    # # determines button color which should be red when user is on that given step
    # wh_type = 'primary' if st.session_state['current_step'] == 1 else 'secondary'
    # ff_type = 'primary' if st.session_state['current_step'] == 2 else 'secondary'
    # lo_type = 'primary' if st.session_state['current_step'] == 3 else 'secondary'
    # sf_type = 'primary' if st.session_state['current_step'] == 4 else 'secondary'

    # step_cols = st.columns(4)    
    # step_cols[0].button('Image',on_click=set_form_step,args=['Jump',1],type=wh_type)
    # step_cols[1].button('Voice',on_click=set_form_step,args=['Jump',2],type=ff_type)        
    # step_cols[2].button('Personality',on_click=set_form_step,args=['Jump',3],type=lo_type)      
    # step_cols[3].button('Knowledge',on_click=set_form_step,args=['Jump',4],type=sf_type)
    
selected = option_menu(
    menu_title= None,
    options=["Image", "Voice", "Personality","Knowledge"],
    icons = ["image", "mic", "person","lightbulb"],
    default_index=0,
    orientation="horizontal",
)
        
### Replace Wizard Form Body with this ###
#def wizard_form_body():
       ###### Step 1: Warehouses ######
if selected == "Image":            
    st.markdown('\n')
    st.markdown('\n')
    st.file_uploader('Upload Image')
    st.markdown('\n')
    st.markdown('\n')    
    file_format_cols = st.columns([8,1.5])                                
    file_format = file_format_cols[0].text_input('Generate Image')
    file_format_cols[1].markdown('\n')
    file_format_cols[1].markdown('\n')
    file_format_cols[1].button('Generate')     
    st.markdown('\n')
    st.markdown('\n')
    
###### Step 2: File Format ######
if selected == "Voice":
    st.markdown('\n')
    st.markdown('\n')
                                    
    st.selectbox('Select Voice',options=['American English Male','American English Female','British English Male','British English Female'])
    st.markdown('\n')
    st.markdown('\n')    
    st.file_uploader('Clone Voice')  
    st.markdown('\n')
    st.markdown('\n')      

###### Step 3: Load Options ######            
if selected == "Personality":                      
    
    st.slider('Empathy',1,10,5)
    st.slider('Positivity',1,10,5)
    st.slider('Intellectual',1,10,5)
    st.slider('Humor',1,10,5)
    st.slider('Confidence',1,10,5)
    
###### Step 4: Source Files ######
if selected == "Knowledge":            
    source_file_container = st.empty()
    with source_file_container.container():
        st.markdown('\n')
        st.markdown('\n')                                
        st.session_state['queued_file'] = st.file_uploader('PDF / Word / Text / MP4')
        st.markdown('\n')
        st.markdown('\n')
        file_format_cols = st.columns([7,1.1])                                
        file_format = file_format_cols[0].text_input('Website / Blogs / Youtube')
        file_format_cols[1].markdown('\n')
        file_format_cols[1].markdown('\n')
        file_format_cols[1].button('Train')   
        st.markdown('\n')
        st.markdown('\n') 
   
        url = 'http://localhost:5000/'

        if st.button("Launch",type="primary"):
            webbrowser.open_new_tab(url)                  
        
# st.markdown('---')

# form_footer_container = st.empty()
# with form_footer_container.container():
    
#     disable_back_button = True if st.session_state['current_step'] == 1 else False
#     disable_next_button = True if st.session_state['current_step'] == 4 else False
    
#     form_footer_cols = st.columns([7,1,1])
    
    
#     form_footer_cols[1].button('Back',on_click=set_form_step,args=['Back'],disabled=disable_back_button)
#     form_footer_cols[2].button('Next',on_click=set_form_step,args=['Next'],disabled=disable_next_button)
    
# # Replace Render Wizard View With This ###
# def render_wizard_view():
#     wizard_form_header()
#     wizard_form_body()



# render_wizard_view()
