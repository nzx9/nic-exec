# nic-exec
### Sri Lankan National Identity Card Data Extractor
#### This script works for <b>both</b> old(9 digits + v/x) and new(12 digits) NIC numbers

## USAGE
use python3

### In Unix (Linux/ Mac)
  ```bash
  python3 nic.py nic_number
  ```
  or
  ```bash
  chmod +x nic.py
  ./nic.py nic_number
  ```
### In Windows
  ```cmd
  python nic.py nic_number
  ```

## MORE INFO   
<b>10 Character NIC | Ex: 987654321V</b>
<ul>
  <li>First 2 characters(98) give the last two digits of birth year(1900 + 98 = 1998)</li>
  <li>Next 3(765) characters give information about gender and birth month and day</li>
  <li>If value of 3rd character to 5th character is higher than 500 that means gender is female, if it less than 500 means gender is male</li>
  <li>If gender is female, have to substract 500 from 3rd character to 5th character(765 - 500), then take the month and day accoding to the number of days in each month(January: 31, February: 29, March: 31, April: 30, ...)</li>
</ul>

<b>12 Character NIC | Ex: 199876543210</b>
<ul>
  <li>First 4 characters(1998) give the birth year</li>
  <li>Next 3(765) characters give information about gender and birth month and day</li>
  <li>If value of 5th character to 8th character(765) is higher than 500 that means gender is female, if it less than 500 means gender is male</li>
  <li>If gender is female, have to substract 500 from value of 5th character to 8th chatacter(765 - 500), then take the month and day accoding to the number of days in each month(January: 31, February: 29, March: 31, April: 30, ...)</li>
</ul>

## Other Implementations
For c++ implementation, please goto [krypto-i9/SL-NIC-Decoder](https://github.com/krypto-i9/SL-NIC-Decoder)
