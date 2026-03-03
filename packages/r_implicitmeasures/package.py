# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImplicitmeasures(RPackage):
	"""Compute Scores for Different Implicit Measures

	A tool for computing the scores for the Implicit Association Test 
    (IAT; Greenwald, McGhee & Schwartz (1998) <doi:10.1037/0022-3514.74.6.1464>) 
    and the Single Category-IAT (SC-IAT: Karpinski & Steinman 
    (2006) <doi:10.1037/0022-3514.91.1.16>). Functions for preparing the data 
    (both for the IAT and the SC-IAT), plotting the results, and obtaining a 
    table with the scores of implicit measures descriptive statistics are 
    provided. 
	"""
	
	cran = "implicitMeasures" 

	version("0.2.1", md5="78bfe5c1d12239086ff93eb3d0bf6a89")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
