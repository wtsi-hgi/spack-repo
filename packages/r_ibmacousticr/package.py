# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIbmacousticr(RPackage):
	"""Connect to Your 'IBM Acoustic' Data

	Authentication can be the most difficult part about
  working with a new API. 'ibmAcousticR' facilitates making a
  connection to the 'IBM Acoustic' email campaign management API
  and executing various queries. The 'IBM Acoustic' API 
  documentation is available at
  <https://developer.ibm.com/customer-engagement/docs/>. This
  package is not supported by 'IBM'.
	"""
	
	cran = "ibmAcousticR" 

	version("0.2.1", md5="ee007c739791d260b9115bd523ec69d2")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-jsonlite@1.7:", type=("build", "run"))
	depends_on("r-httr@1.4.1:", type=("build", "run"))
	depends_on("r-xml@3.99.0.5:", type=("build", "run"))
