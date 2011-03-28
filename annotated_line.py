#! /usr/bin/python
#
#
import random
# Generate the beginning HTML and Javascript
print """
<html>
  <head>
    <script type='text/javascript' src='https://www.google.com/jsapi'></script>
    <script type='text/javascript'>
      google.load('visualization', '1', {'packages':['annotatedtimeline']});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = new google.visualization.DataTable();
        data.addColumn('date', 'Date');
        data.addColumn('number', 'Sold Pencils');
        data.addColumn('string', 'title1');
        data.addColumn('string', 'text1');
        data.addColumn('number', 'Sold Pens');
        data.addColumn('string', 'title2');
        data.addColumn('string', 'text2');
        data.addRows(["""
for i in range(1,31) :
    if i == 4 :
        print "          [new Date(2008, 1 ,4), 75284, undefined, undefined, 14334, 'Out of Stock','Ran out of stock on pens at 4pm'],"
    elif i == 5 :
        print "          [new Date(2008, 1 ,5), 41476, 'Bought Pens','Bought 200k pens', 66467, undefined, undefined],"
    else :
        print "          [new Date(2008, 1 ,",i,"),", random.randrange(60000), ", undefined, undefined,", random.randrange(60000), ", undefined, undefined],"

    
#          [new Date(2008, 1 ,2), 14045, undefined, undefined, 20374, undefined, undefined],
#         [new Date(2008, 1 ,3), 55022, undefined, undefined, 50766, undefined, undefined],
#          [new Date(2008, 1 ,4), 75284, undefined, undefined, 14334, 'Out of Stock','Ran out of stock on pens at 4pm'],
#          [new Date(2008, 1 ,5), 41476, 'Bought Pens','Bought 200k pens', 66467, undefined, undefined],
#          [new Date(2008, 1 ,6), 33322, undefined, undefined, 39463, undefined, undefined]
# Note that this next line does not have a comma at the end.
print "          [new Date(2008, 1 , 31),", random.randrange(60000), ", undefined, undefined,", random.randrange(60000), ", undefined, undefined]"
print """
        ]);

        var chart = new google.visualization.AnnotatedTimeLine(document.getElementById('chart_div'));
        chart.draw(data, {displayAnnotations: true});
      }
    </script>
  </head>

  <body>
    // Note how you must specify the size of the container element explicitly!
    <div id='chart_div' style='width: 700px; height: 240px;'></div>

  </body>
</html>
"""
