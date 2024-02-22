# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcods(RPackage):
	"""Data Analysis for ODS and Case-Cohort Designs with
Interval-Censoring

	Sieve semiparametric likelihood methods for analyzing 
 interval-censored failure time data from an outcome-dependent sampling (ODS) 
 design and from a case-cohort design. 
 Zhou, Q., Cai, J., and Zhou, H. (2018) <doi:10.1111/biom.12744>; 
 Zhou, Q., Zhou, H., and Cai, J. (2017)  <doi:10.1093/biomet/asw067>.
	"""
	
	cran = "ICODS" 

	version("1.1", md5="501db8845e14b6d691f5fb702eeb3cc4")

	depends_on("r-mass", type=("build", "run"))
