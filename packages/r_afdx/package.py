# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfdx(RPackage):
	"""Diagnosis Performance Using Attributable Fraction

	Estimate diagnosis performance (Sensitivity, Specificity, 
    Positive predictive value, Negative predicted value) of a diagnostic test
    where can not measure the golden standard but can estimate it using the 
    attributable fraction. 
	"""
	
	homepage = "https://github.com/johnaponte/afdx"
	cran = "afdx" 

	version("1.1.1", md5="764c0a32a0091207aa38d3274e0d3100")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
