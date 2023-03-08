
import xml.etree.ElementTree as ET
data='''<person>
	<name>Dan</name>
	<phone type='intl'>
		0753944114
	</phone>
	<email hide='yes'/>
</person>'''


tree=ET.fromstring(data)
print('Name: ',tree.find('name').text)
print('Attr: ',tree.find('email').get('hide'))
