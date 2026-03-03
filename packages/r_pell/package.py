# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPell(RPackage):
	"""Data About Historic Pell Grant Distribution in the US

	Historic Pell grant data as provided by the US Department of Education. 
    This package contains data about how much pell grant was awarded by which institution in 
    which year. 
    This data comes from the US Department of Education. Raw data can be downloaded from here: <https://www2.ed.gov/finaid/prof/resources/data/pell-institution.html>.
	"""
	
	homepage = "https://github.com/Curious-Joe/pell"
	cran = "pell" 

	version("0.1.0", md5="639b06df4aca8927660f39c4accc7e5d")

	depends_on("r@2.10:", type=("build", "run"))
