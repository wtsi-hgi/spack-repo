# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBoxplotdbl(RPackage):
	"""Double Box Plot for Two-Axes Correlation

	Correlation chart of two set (x and y) of data.  
  Using Quartiles with boxplot style. 
  Visualize the effect of factor. 
	"""
	
	cran = "boxplotdbl" 

	version("1.4.0", md5="4c4055fd42d721beebc3952020a8c782")

