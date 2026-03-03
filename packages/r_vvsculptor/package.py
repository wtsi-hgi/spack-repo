# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVvsculptor(RPackage):
	"""Apply Manipulations to Data Frames

	Provides a set of functions for manipulating data frames in accordance with specific business rules. 
    In addition, it includes wrapper functions for commonly used functions from the popular 'tidyverse' package, 
    making it easy to integrate these functions into data analysis workflows. 
    The package is designed to streamline data preprocessing and help users quickly and efficiently 
    perform data transformations that are specific to their business needs.
	"""
	
	cran = "vvsculptor" 

	version("0.4.10", md5="2019460b61a261163b2c886ef6070843")

	depends_on("r-dplyr", type=("build", "run"))
