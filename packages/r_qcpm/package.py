# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcpm(RPackage):
	"""Quantile Composite Path Modeling

	Implements the Quantile Composite-based Path Modeling approach 
	(Davino and Vinzi, 2016 <doi:10.1007/s11634-015-0231-9>; 
	 Dolce et al., 2021 <doi:10.1007/s11634-021-00469-0>). The method complements the traditional PLS Path Modeling approach, analyzing the entire distribution of outcome variables and, therefore, overcoming the classical exploration of only average effects. It exploits quantile regression to investigate changes in the relationships among constructs and between constructs and observed variables.
	"""
	
	cran = "qcpm" 

	version("0.3", md5="0c93923d8a1addbb322cf065ea18e469")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-csem", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
