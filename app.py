import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.sidebar.title("Sofware educativo para el estudio  de fenómenos ondulatorios")
opl=st.sidebar.radio("", ["Ondas estacionarias","Interferencia de ondas","Onda general"])
if opl=="Ondas estacionarias":
  st.title(opl)
  n=st.slider("",1,10)
  x=np.linspace(0,2*np.pi,150)
  #st.write(x)
  y=np.sin(n*x/2)
  fig, ax = plt.subplots()
  ax.plot(x,y)
  st.pyplot(fig)
