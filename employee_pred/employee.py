#importing recquired libraries
from dash import Dash,html,dcc,dash_table,callback,State,Input,Output
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

df=read.csv("data.csv")
df0=read.csv("data.csv)

leb=LabelEncoder()
df["Gender"]=leb.fit_transform(df["Gender"])
df["Citizen"]=leb.fit_transform(df["Citizen"])
df["Povert_index"]=leb.fit_transform(df["Povert_index"])
df["Sales"]=leb.fit_transform(df["Sales"])
y=df["Performance"]
df2=df0.head()
p=df[["Performance","Age","Citizen"]].corr()
q=df[["Performance","Povert_index","Gender"]].corr()
p
model=LinearRegression()
x=df[["Age","Citizen","Sales","Povert_index","Gender","Sickoff"]]
fi= model.fit(x,y)
fi.intercept_
prediction=fi.predict([[23,0,1,1,0,2]])

title=dbc.Row([dbc.Card([html.H2(["PREDICTION OF EMPLOYEE % PERFORMANCE "],className="card-header",style={"color":"rgb(255,255,255)"})],className="bg-dark",)],style={"paddingLeft":"2%","width":"100vw"})
expla=dbc.Row([dbc.Card([dbc.CardHeader([html.H5("Purpose",style={"font-size":"20px","color":"rgb(192,192,192)"})]),dbc.CardBody([html.P(["The aim of this project is to help companies who want to employ  persons on a permanent basis should consider employing them on contract terms first. Then use this app to evaluate their performance.Those with exceptional performance should be considered.The Data was collected using google forms. "],style={"font-size":"20px","color":"rgb(192,192,192)"}),html.P(
    "Performance being our depedent variable(performance being predicted based on sales,gender,age,citizenship,number of sickoff days and poverty index)",style={"font-size":"20px","color":"rgb(192,192,192)"})])],className="bg-dark")])
corr_tab1=dbc.Card([dbc.CardHeader([html.H5("correlation table",style={"font-size":"20px","color":"rgb(192,192,192)"})]),dbc.CardBody([html.Div((dash_table.DataTable(p.to_dict('records'),style_data={"background-color":"rgb(0,0,0)","color":"rgb(0,0,255)"}))),dbc.CardFooter("@aronconsultancy")])],color="dark",style={"width":"50vw"})
corr_tab2=dbc.Card([dbc.CardHeader([html.H5("correlation table",style={"font-size":"20px","color":"rgb(192,192,192)"})]),dbc.CardBody([html.Div((dash_table.DataTable(q.to_dict('records'),style_data={"background-color":"rgb(0,0,0)","color":"rgb(0,0,255)"}))),dbc.CardFooter("@aronconsultancy")])],color="dark",style={"width":"50vw"})
data_sample_tab=dbc.Card([dbc.CardHeader([html.H5("Sample data table",style={"font-size":"20px","color":"rgb(192,192,192)"})]),dbc.CardFooter(""),
                          dbc.CardBody([dash_table.DataTable(df2.to_dict('records'),style_data={"background-color":"rgb(0,0,0)","color":"rgb(0,0,255)"})])],color="dark",style={"width":"42vw"})

#plots
fig=px.bar(df0,x=["Gender","Citizen","Sales","Povert_index"],y="Performance",color='Gender')
fig2=px.scatter_3d(df0,x="Sickoff",z="Age",y="Performance",color="Gender")
fig3=px.imshow(df)
fig4=px.bar(df0,x="Povert_index",y="Performance",color='Povert_index')
fig5=px.scatter(df0,x="Age",y="Performance",color="Sickoff")
scatter_age_Per=bar_for_povert_fig=dbc.Card([dbc.CardHeader([html.H5("Scatter plot for performance, age,sickoff",style={"font-size":"20px","color":"rgb(192,192,192)"},)]),dbc.CardBody([dcc.Graph(figure=fig5)])],color="dark")
bar_for_povert_fig=dbc.Card([dbc.CardHeader([html.H5("performance povert bar graph",style={"font-size":"40px%","color":"rgb(255,255,255)"})]),dbc.CardBody([dcc.Graph(figure=fig4)])],color="dark")
bar_for_sales_fig=dbc.Card([dbc.CardHeader([html.H5("Heatmap of all the variables",style={"font-size":"40px%","color":"rgb(255,255,255)"})]),dbc.CardBody([dcc.Graph(figure=fig3)])],color="dark")
bar_for_citizen_fig=dbc.Card([dbc.CardHeader([html.H5("3D cluster plot of age,sickoff and performance ",style={"font-size":"40px%","color":"rgb(255,255,255)"})]),dbc.CardBody([dcc.Graph(figure=fig2)])],color="dark")
bar_for_gender_fig=dbc.Card([dbc.CardHeader([html.H5("Count plot of input values",style={"font-size":"40px%","color":"rgb(255,255,255)"})]),dbc.CardBody([dcc.Graph(figure=fig)])],color="dark")
pre_card=dbc.Card([html.Div([html.H6("Age",style={"marginLeft":"30%","font-size":"18px%","color":"rgb(255,255,255)","paddingLeft":"%","width":""}),
                   dcc.Input(id="a",type="number",min=14,max=90,style={"marginLeft":"25%","border":"2%auto","border-radius":"20%","paddingLeft":"25%","width":"15vw"}),
                   html.H6("Citizen[local input 1,foreign input 0]",style={"marginLeft":"15%","font-size":"18px","color":"rgb(255,255,255)","paddingLeft":"","width":""}),
                   dcc.Input(id="c",type="number",min=0,max=1,style={"marginLeft":"25%","border":"2%auto","border-radius":"20%","paddingLeft":"25%","width":"15vw"}),
                   html.H6("sales made during contract[good input 2,average input 0,below average input 1]",style={"marginLeft":"15%","font-size":"18px","color":"rgb(255,255,255)","paddingLeft":"","width":""}),
                   dcc.Input(id="s",type="number",min=0,max=2,style={"marginLeft":"25%","border":"2%auto","border-radius":"20%","paddingLeft":"25%","width":"15vw"}),
                   html.H6("povert index[poor input  0,welloff input 1] ",style={"marginLeft":"15%","font-size":"18px","color":"rgb(255,255,255)","paddingLeft":"","width":""}),
                   dcc.Input(id="p",type="number",min=0,max=1,style={"marginLeft":"25%","border":"2%auto","border-radius":"20%","paddingLeft":"25%","width":"15vw"})
                   ,html.H6("Gender[male input 1,female input 0",style={"marginLeft":"15%","font-size":"18px","color":"rgb(255,255,255)","paddingLeft":"","width":""}),
                   dcc.Input(id="g",type="number",min=0,max=1,style={"marginLeft":"25%","border":"2%auto","border-radius":"20%","paddingLeft":"25%","width":"15vw"}),
                   html.H6("sick off days",style={"marginLeft":"30%","font-size":"18px","color":"rgb(255,255,255)","paddingLeft":"","width":""}),
                   dcc.Input(id="si",type="number",min=0,max=5000,style={"marginLeft":"25%","border":"2%auto","border-radius":"20%","paddingLeft":"25%","width":"15vw"}),

                   dbc.Button(id="submit",children="PREDICT",style={"marginLeft":"70%","border":"2%auto","border-radius":"20%","background-color":"rgb(220,0,0)","width":"10vw"}),
                   ])],color="dark")
anime=html.Div([],)
outpre=dbc.Card([html.Div(id="predout") ,html.P("OUTPUT WILL COMEOUT HERE")],style={"background-color":"rgb(192,192,192)"})
ro_for_g_c=dbc.Row([dbc.Col([bar_for_gender_fig]),dbc.Col([bar_for_citizen_fig])],className="two columns g-0",style={"paddingLeft":"2%","width":"100vw"})
ro_for_s_p = dbc.Row([dbc.Col([bar_for_sales_fig]), dbc.Col([bar_for_povert_fig])], className="two columns g-0",style={"paddingLeft":"2%","width":"100vw"})
ro_for_scatter_p = dbc.Row([dbc.Col([scatter_age_Per],width=9), ],style={"paddingLeft":"2%","width":"100vw"})
#card_tab3=dbc.Card([dbc.CardHeader("PEDICT")],color="primary")


app=Dash(__name__,external_stylesheets=[dbc.themes.ZEPHYR])
app.title="salesemployeeperformance"
app.layout=html.Div(children=[dbc.Navbar([dbc.DropdownMenu([dbc.DropdownMenuItem([dbc.NavLink("About me",href="https://www.blogger.com/profile/07293138198715749524")]),
    dbc.DropdownMenuItem([dbc.NavLink("visit my github",href="https://github.com/")]),
   dbc.DropdownMenuItem([dbc.NavLink("Linkdn",href="https://www.linkedin.com/in/wanga-harron-464371161/")]),
  dbc.DropdownMenuItem([dbc.NavLink("visit my website",href="https://stats-guru.blogspot.com/?m=1")])],label="MENUBAR",style={"bakground-color":"rgb(192,192,192)"}),html.H4("Ar0NConsuLTAncy LTD",style={"color":"rgb(220,20,60)","font-size":"30px","paddingLeft":"50%"})],style={"paddingLeft":"2%","height":"8vh","width":"100vw",},className="bg-dark"),
  dcc.Tabs(id="tabs_id",children=[dcc.Tab(value="T1",label="HOME",className="bg-primary",style={"marginLeft":"2%","border":"2%auto","border-radius":"20%","background-color":"rgb(220,0,0)","width":"10vw"}),
  dcc.Tab(value="T2",label=" CLICK FOR CORRELATION",className="bg-danger",style={"marginLeft":"2%","border":"2%auto","border-radius":"20%","background-color":"rgb(220,0,0)","width":"10vw"}),
  dcc.Tab(value="T3",label="CLICK FOR PREDICT",className="bg-warning",style={"marginLeft":"2%","border":"2%auto","border-radius":"20%","background-color":"rgb(220,0,0)","width":"10vw"})],style={"width":"100vw"}),html.Div(id="click_tab")])
@app.callback(
    Output("predout","children"),
    [Input("submit","n_clicks")],
    [State("a","value"),
     State("c","value"),
     State("s","value"),
     State("p","value"),
     State("g","value"),
     State("si","value")])
def update_output(n_clicks,a,c,s,p,g,si):
    if n_clicks==0:
        return " "
    else:
        ma=fi.predict([[a,c,s,p,g,si]])
        return html.H5("THE PREDICTED % PERFORMANCE IS:{}".format(ma),style={"color":"rgb(255,0,0)","font-size":"40px"})


@app.callback(Output("click_tab","children"),
              Input("tabs_id","value")
             # State("tabs_id","value"))
             )
def update_content(tab):
    if tab=="T1":
        return  html.Div([dbc.Row([title],style={"paddingLeft":"2%","width":"100vw"}),dbc.Row([dbc.Col([expla]),dbc.Col([data_sample_tab])],className="two columns g-0",style={"paddingLeft":"2%","width":"100vw"}),ro_for_g_c,ro_for_s_p],style={"background-color":"rgb(255,215,0)"})
    if tab=="T2":
        return html.Div([ro_for_scatter_p,dbc.Row([corr_tab1,corr_tab2])],style={"background-color":"rgb(255,215,0)"})
    if tab=="T3":
        return html.Div([dbc.Row([dbc.Col([pre_card],width=5,style={"margin-left":"10px"}),dbc.Col([outpre],width=3)],className="two columns g-0",style={"paddingLeft":"2%","width":"100vw"})],className="bg-dark")

    else :
        return html.Div([dbc.Row([title],style={"paddingLeft":"2%","width":"100vw"}),dbc.Row([dbc.Col([expla]),dbc.Col([data_sample_tab])],className="two columns g-0",style={"paddingLeft":"2%","width":"100vw"}),ro_for_g_c,ro_for_s_p],style={"background-color":"rgb(255,215,0)"})


if __name__=="__main__":
    app.run_server()
