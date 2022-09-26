from queue import *
# Function to find page faults using FIFO
def pF(pages, n, capacity):
	
	s = set()

	# To store the pages in FIFO manner
	indexes = Queue()

	# Start from initial page
	page_faults = 0
	for i in range(n):
		
		# Check if the set can hold
		# more pages
		if (len(s) < capacity):
			
			# Insert it into set if not present
			# already which represents page fault
			if (pages[i] not in s):
				s.add(pages[i])

				# increment page fault
				page_faults += 1

				# Push the current page into
				# the queue
				indexes.put(pages[i])

		# If the set is full then need to perform FIFO
		# i.e. remove the first page of the queue from
		# set and queue both and insert the current page
		else:
			
			# Check if current page is not
			# already present in the set
			if (pages[i] not in s):
				
				# Pop the first page from the queue
				val = indexes.queue[0]

				indexes.get()

				# Remove the indexes page
				s.remove(val)

				# insert the current page
				s.add(pages[i])

				# push the current page into
				# the queue
				indexes.put(pages[i])

				# Increment page faults
				page_faults += 1

	return page_faults

# Driver code
if __name__ == '__main__':
    pages = []
    m = int(input("Enter number of elements : "))
    for i in range(0, m):
        ele = int(input("Enter the element no."+str(i+1)+": "))
        pages.append(ele)
            
    n = len(pages)
    capacity = int(input("Enter the page capacity: "))
    fault=pF(pages, n, capacity)
    hit= m - fault
    print("No. of Faults: ", fault)
    print("No. of hits: ", hit)