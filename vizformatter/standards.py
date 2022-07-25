# importing date class from datetime module
from datetime import date
# creating the date object of today's date
todays_year = date.today().year


def layout_plotly(height, width, font_size):

    ''' Return the Standard layout for plotly graphs and the author sign


    :param height: Canvas height measured in px

    :param width: Canvas width measured in px

    :param font_size: Base fontsize of the Canva,
    where title size is +5, legend+ size is +2 and annotations size is -1


    :return: Tuple with author sign and layout respectively

    :reference: For more graph standarized https://plotly.com/python/plotly-express/
    
    '''

    # Author template to reference the graph
    author = "Published at <a href='https://www.robguilar.com'>robguilar&#8482;</a><br>Made by:  R. Aguilar, "+str(todays_year)
    heightimg = height
    widthimg = width
    fontimg = font_size # Default sizes between 14-17
    colorfont= "#636363" # Black: #000000 , # White: "#FFFFFF" , # Default font color: #636363
    backcolor= "#FFFFFF"
    xzero_linec = "#fff" # Default line color: #3D5165
    yzero_linec = "#fff"

    # Author Sign Annotation set as dictionary
    sign = {"text":author,"align":"right","visible":True,"xref":"paper","yref":"paper","x":1,"y":-0.11,"showarrow":False,"font.size":fontimg-1}

    # Base layout set as dictionary
    layout = {"font": {"size": fontimg ,
                        "color": colorfont,
                        "family": "segoe ui light"},
                "title":{'y':0.935,
                        'x':0.4,
                        "yref":"container",
                        'xanchor': 'center',
                        'yanchor': 'top',
                        "font.family":"bahnschrift light",
                        "font.color":"#202020",
                        "font.size":fontimg+5,
                        "pad.b":15, # to avoid overlap with graph
                        "pad.l":1},
                "showlegend": True,
                "legend":{"font.size": fontimg,
                        "bordercolor": "#F70000",
                        "itemclick":"toggleothers",
                        "itemwidth": 30,
                        "itemdoubleclick":False,
                        "title.side": "top",
                        "title.font.color": "#202020",
                        "title.font.size": fontimg+2,
                        "x":1.05}, # distance with the plot default to 1.02
                "margin":{"b": 65,
                        "l": 65,
                        "r": 65,
                        "t": 80,
                        "pad": 0},
                "autosize":True,
                "width": widthimg,
                "height": heightimg,
                "separators": ". ",
                "paper_bgcolor": backcolor,
                "plot_bgcolor": backcolor,
                "autotypenumbers": "convert types",
                "hoverdistance":50, #Distance between cursor and hover announce
                "hoverlabel":{"align":"left",
                            "bordercolor":"#fff",
                            "bgcolor":"#3D5165",
                            "font.color":"#FFFFFF",
                            "font.family":"segoe ui light",
                            "font.size":fontimg},
                "grid":{"pattern":"coupled",
                        "roworder":"bottom to top",
                        "xgap":0.5,
                        "ygap":0.5,
                        "xside":"bottom"},
                "newshape":{"line.color":"#3D5165",
                            "line.width":1.5,
                            "opacity":0.7},
                "activeshape.opacity":0.7,
                "xaxis": {"gridcolor":"#fff",
                        "spikecolor":"#DEDEDE", # Horizontal line hovered 
                        "spikethickness":1.5,
                        "showspikes": False,
                        "anchor":"free",
                        "position":0,
                        "showgrid":False,
                        "tickcolor":"#FD0000",
                        "ticklabelposition": "outside",
                        "title.standoff": 10, #Distance between axis title and axis labels
                        "zeroline": True,
                        "zerolinecolor": xzero_linec,
                        "zerolinewidth": 1.5,
                        "automargin": True},
                "yaxis": {"gridcolor":"#EDEDED",
                        "spikecolor":"#DEDEDE", # Horizontal line hovered
                        "spikethickness":1.5,
                        "showspikes": False,
                        "ticklabelposition": "outside",
                        "tickprefix": "", #Label prefix
                        "ticksuffix": "", # Label sufix
                        "title.standoff": 10, #Distance between axis title and axis labels
                        "zeroline": True,
                        "zerolinecolor": yzero_linec,
                        "zerolinewidth": 1.5,
                        "automargin": True}
                }

    return sign, layout










