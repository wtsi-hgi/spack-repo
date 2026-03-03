# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActlifer(RPackage):
	"""Creating Actuarial Life Tables

	Contains data and functions that can be used to make 
  actuarial life tables. Each function adds a column to the inputted dataset for
  each intermediate calculation between mortality rate and life expectancy. Users can 
  run any of our functions to complete the life table until that step, or run
  lifetable() to output a full life table that can be customized to remove optional columns. 
  Methods for creating lifetables are as described in Zedstatistics (2021) <https://www.youtube.com/watch?v=Dfe59glNXAQ>.
	"""
	
	homepage = "https://github.com/g-rade/actLifer"
	cran = "actLifer" 

	version("1.0.0", md5="86773f3bfe8d421b0e66c35efca9b392")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
