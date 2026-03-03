# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfc(RPackage):
	"""Cause-Specific Framework for Competing-Risk Analysis

	Numerical integration of cause-specific survival curves to arrive at cause-specific cumulative incidence functions,
  with three usage modes: 1) Convenient API for parametric survival regression followed by competing-risk analysis, 2) API for
  CFC, accepting user-specified survival functions in R, and 3) Same as 2, but accepting survival functions in C++. For 
  mathematical details and software tutorial, see Mahani and Sharabiani (2019) <DOI:10.18637/jss.v089.i09>. 
	"""
	
	cran = "CFC" 

	version("1.2.0", md5="744701758c985e340969323062def50c")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
