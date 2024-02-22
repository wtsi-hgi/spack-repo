# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActfrag(RPackage):
	"""Activity Fragmentation Metrics Extracted from Minute Level
Activity Data

	Recent studies haven shown that, on top of total daily active/sedentary volumes, the time 
  accumulation strategies provide more sensitive information. This package provides functions to extract 
  commonly used fragmentation metrics to quantify such time accumulation strategies based on minute level 
  actigraphy-measured activity counts data. 
	"""
	
	homepage = "https://github.com/junruidi/ActFrag"
	cran = "ActFrag" 

	version("0.1.1", md5="78794c1a49a248d494dabad61d269b20")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-accelerometry", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ineq", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
