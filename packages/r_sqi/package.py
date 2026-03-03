# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqi(RPackage):
	"""Soil Quality Index

	The overall performance of soil ecosystem services and productivity greatly relies on soil health, making it a crucial indicator. The evaluation of soil physical, chemical, and biological parameters is necessary to determine the overall soil quality index. In our package, three commonly used methods, including linear scoring, regression-based, and principal component-based soil quality indexing, are employed to calculate the soil quality index. This package has been developed using concept of Bastida et al. (2008) and Doran and Parkin (1994) <doi:10.1016/j.geoderma.2008.08.007> <doi:10.2136/sssaspecpub35.c1>.  
	"""
	
	cran = "SQI" 

	version("0.1.0", md5="588e02f55af85105042509a49b6e7e07")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-olsrr", type=("build", "run"))
	depends_on("r-factominer", type=("build", "run"))
