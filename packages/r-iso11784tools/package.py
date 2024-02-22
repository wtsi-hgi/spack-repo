# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIso11784tools(RPackage):
	"""ISO11784 PIT Tag ID Format Converters

	Some tools to assist with converting International Organization for Standardization (ISO) standard 11784 (ISO11784) animal ID codes between 4 recognised formats commonly displayed on Passive Integrated Transponder (PIT) tag readers.
    The most common formats are 15 digit decimal, e.g., 999123456789012, and 13 character hexadecimal 'dot' format, e.g., 3E7.1CBE991A14. These are referred
    to in this package as isodecimal and isodothex. The other two formats are the raw hexadecimal representation of the ISO11784 binary
    structure (see <https://en.wikipedia.org/wiki/ISO_11784_and_ISO_11785>). There are two 'flavours' of this format, a left and a right variation. Which flavour
    a reader happens to output depends on if the developers decided to reverse the binary number or not before converting to hexadecimal, a decision based on 
    the fact that the PIT tags will transmit their binary code Least Significant Bit (LSB) first, or backwards basically.
	"""
	
	cran = "ISO11784Tools" 

	version("1.1.4", md5="de8b1a1e5821de4eee41346e4a29baaf")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
