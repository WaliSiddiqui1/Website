#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 22:48:13 2024

@author: saminakashif
"""
from PIL import Image
from PIL import ImageOps
import requests
import streamlit as st
from streamlit_option_menu import option_menu
    
st.set_page_config(page_title = "A website for Sophia", page_icon = ":heart:", layout = 'wide')

with st.sidebar:
    selected = option_menu(
        menu_title = 'Menu',
        options = ['Overview', 'Pictures', 'Haiku', 'Code'],
        icons = ['/Users/saminakashif/Downloads/arrow-through-heart-fill.svg'],
        menu_icon = '/Users/saminakashif/Downloads/arrow-through-heart-fill.svg',
        default_index = 0,
        )

if selected == 'Overview':
    with st.container():
        st.subheader("Sophia's website")
        st.title("A website I coded for my love")
        st.write("I have put a few of my favorite photos, moments and memories of us as well as a little haiku")
        st.markdown("https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExZGlpd3k2NnZpZnZndW05MzRhY2Nnd3VkNXV3cXBobzhsMGw0cGkxOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/T1TqR5TT62mVG/giphy.gif")
    
if selected == 'Pictures':
    st.title(f"Welcome to the {selected} page")
    with st.container():
        st.write("---")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("A series of photos")
            st.write("Here I've added a few photos that I love of you and I.")

    with st.container():
        st.write("---")
        
    for i in range (1,21):
        col1, col2, col3 = st.columns(3)

        try:
            img = Image.open(f"Sophia{i}.jpg")
            img = ImageOps.exif_transpose(img)

            if i == 1:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, caption='',  width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Our first picture together!</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 2: 
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>A very special night since this is when we became boyfriend and girlfriend</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 3: 
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>We don't take many silly photos, but this is one of them I love</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 4: 
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>You know I had to put my favorite picture of you in here</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 5: 
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>A beautiful moment from our crazy trip that made it all worth it</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 6: 
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>A microcosmic picture displaying all the great meals we shared</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 7: 
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                with col3:
                    st.write('')
            elif i == 8:
                    with col1:
                        st.write('')
                    with col2:
                        st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                        st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Two photos of my gorgeous girl on Eid</p>", unsafe_allow_html=True)
                    with col3:
                        st.write('')
            elif i == 9:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>You look very British here, Oxford-esque</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 10:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Spring weekend!</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 11:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>This was so fun, Holi shit did we get wet 😉 </p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 15:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Just some more pictures of my stunning girlfriend </p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 16:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'> Our little beach scavenger </p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 17:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Sophia eating ice cream, a tale as old as time </p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 18:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'> Our best Flynn Rider impersonation on our little hike </p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 19:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'>Not the best photo of the red panda but our speed run of the zoo was so fun I had to add this </p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            elif i == 20:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                    st.markdown("<p style='text-align: center; font-size: 18px; color: white;'> An eventful night, but one that commemorates your graduation!</p>", unsafe_allow_html=True)
                with col3:
                    st.write('')
            else:
                with col1:
                    st.write('')
                with col2:
                    st.image(img, width=320, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
                with col3:
                    st.write('')
        
        except Exception as e:
                st.write(f"Error: {e}")
    
if selected == 'Haiku':
    st.title(f"Welcome to the {selected} page")
    with st.container():
        custom_subheader_text = """
<p style='font-size: 15px;'>
There is so much I can say about you. I said a lot of it in my love letter, 
but it didn't feel enough. I don't think it ever will, 
but here is another piece of writing to show my love.
</p>
"""

        st.markdown(custom_subheader_text, unsafe_allow_html=True)
        st.write("---")
        st.markdown("<p style='text-align: center; font-size: 30px; color: blue;'> Sophia, golden</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 30px; color: blue;'> I melt to her true, pure smile</p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; font-size: 30px; color: blue;'> My brain, it turns off</p>", unsafe_allow_html=True)
        
if selected == 'Code':
    st.title(f"Welcome to the {selected} page")
    with st.container():
        custom_subheader_text = """
<p style='font-size: 20px;'>
If you were curious, I have attached the code to this page.
</p>
"""
        st.markdown("https://github.com/WaliSiddiqui1/Website/edit/main/Sophia_Website.py")
