# UCS_Algortihm
Uniform Cost Search Algorithm Implementation.

The most important decision I made while doing this assignment was to use the Priority Queue. Because the priority queue logic is appropriate for Uniform Cost Search.
In Uniform Cost Search the minimum cost for the path is calculated, on the other hand, the get method in the priority queue does what it needs to be done and it removes 
the item which has the least priority. Hence, we don’t need any other method to do this. To elaborate a little more on uniform cost search I would like to use an example
from our data. For example, let’s think about the İstanbul-Kayseri path. Our start node would be İstanbul and our goal would be Kayseri. So, for the first iteration, we 
should go to the Çanakkale because its cost is the minimum. And for the second iteration, we should go to the Eskişehir because of the same logic. We cannot go to the 
Balıkesir from the Çanakkale because Balıkesir’s total cost is more than Eskişehir’s cost. To sum up we could say: The Uniform Cost Search is the search algorithm that 
obtains a path via total cost.


Also, I would like the mention another python item that I used. Dictionaries are the perfect match to return graph for the build_graph method. I set the cities as keys and 
the distances as values.

Finally, I used try-exception blocks to handle the FileNotFound, CityNotFound exceptions and I handle the general exception just in case.
