# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmtr(RPackage):
	"""Easily Apply Formats to Data

	Contains a set of functions that can be used to apply
  formats to data frames or vectors.  The package aims to provide 
  functionality similar to that of SAS® formats. Formats are assigned to
  the format attribute on data frame columns.  Then when the fdata() 
  function is called, a new data frame is created with the column data
  formatted as specified.  The package also contains a value() function
  to create a user-defined format, similar to a SAS® user-defined format.
	"""
	
	homepage = "https://fmtr.r-sassy.org"
	cran = "fmtr" 

	version("1.6.3", md5="e9c4d3a0c7f0ea56a92ba65867c5e63e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-common", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
