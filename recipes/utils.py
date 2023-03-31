from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    #create a BytesIO buffer for the image
    buffer = BytesIO()

    #create a plot with a bytesIO object as a file-like object. Set format to png
    plt.savefig(buffer, format='png')

    #set cursor to the beginning of the stream
    buffer.seek(0)

    #retrieve the content of the file
    image_png=buffer.getvalue()

    #encode the bytes-like object
    graph=base64.b64encode(image_png)

    #decode to get the string as output
    graph=graph.decode('utf-8')

    #free up the memory of buffer
    buffer.close()

    #return the image/graph
    return graph

#chart_type: user input type of chart,
#data: pandas dataframe
def get_chart(chart_type, ingredients, number_recipes, **kwargs):
   #switch plot backend to AGG (Anti-Grain Geometry) - to write to file
   #AGG is preferred solution to write PNG files
   plt.switch_backend('AGG')

   #specify figure size
   fig, ax = plt.subplots(figsize=(7,3))

   ax.set(title='Number of recipes that have the ingredients from searched recipe')
   plt.show()

   #select chart_type based on user input from the form
   if chart_type == '#1':
       #plot bar chart between ingredient on x-axis and number recipes on y-axis
       plt.bar(ingredients, number_recipes)

   elif chart_type == '#2':
       #generate pie chart based on number recipes with each ingredient
       #The ingredients are sent from the view as labels
       labels=kwargs.get('labels')
       plt.pie(number_recipes, labels=labels)

   elif chart_type == '#3':
       #plot line chart based on ingredients on x-axis and number recipes on y-axis
       plt.plot(ingredients, number_recipes)

   else:
       print ('unknown chart type')

   #specify layout details
   plt.tight_layout()

   #render the graph to file
   chart = get_graph()
   return chart
