# Geographic Coordinate Converter
#### Video Demo:  <https://www.youtube.com/watch?v=MulLMLVqZrE>
#### Description:
Many times, in works of cartography, topography or engineering in general we receive a list of geographic coordinates in decimal degrees format, but it is required that they be expressed in others formats like Degrees Minutes and Seconds (ex. 30°45’36”S).

Although the conversion calculation is simple, the process can be laborious when many points need to be converted. For this, in a very practical way, the system called “Geographic Coordinate Converter” was developed. This application is capable of reading data in a CSV file containing the ID, Latitude and Longitude fields.

This system was developed using the Python programming language using the Pandas library. The script is build with six functions: main, read_csv_file, coordinate_calc, coordinate_gms, check_number e print_csv.

#### 1)	main: it is a function responsible for to make the management of the script and to call others functons.
#### 2)	read_csv_file: it is a function responsible for reading the csv file and making a new dataframe using pandas.
#### 3)	coordinate_calc: it is a function responsible for the calculation of degrees, minutes and seconds values.
#### 4)	coordinate_gms: it is a function responsible for making a string with degrees, minutes and seconds values.
#### 5)	check_number: it is a function responsible for checking if a number is bigger or smaller than 10. It is necessary to use the number zero in front of numbers smaller than 10.
#### 6)	Print_csv: it is a function responsible for to build another csv file, but here with coordinates in degrees, minutes and seconds format.

Finally, as a result, the tool generates a new CSV file containing the original fields, plus Latitude and Longitude fields in the format of Degrees Minutes and Seconds.

As a next step, I would like to implement a menu with conversion options. For exemple from Decimal Degrees to Degrees Minutes and Seconds and the reverse operation.
