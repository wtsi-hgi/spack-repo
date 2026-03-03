# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgretci(RPackage):
	"""Exploration and Graphics for RivEr Trends Confidence Intervals

	Collection of functions to evaluate uncertainty of results from
    water quality analysis using the Weighted Regressions on Time Discharge and
    Season (WRTDS) method. This package is an add-on to the EGRET package that
    performs the WRTDS analysis. The WRTDS modeling
    method was initially introduced and discussed in Hirsch et al. (2010) <doi:10.1111/j.1752-1688.2010.00482.x>,
    and expanded in Hirsch and De Cicco (2015) <doi:10.3133/tm4A10>. The 
    paper describing the uncertainty and confidence interval calculations 
    is Hirsch et al. (2015) <doi:10.1016/j.envsoft.2015.07.017>.
	"""
	
	homepage = "https://github.com/USGS-R/EGRETci"
	cran = "EGRETci" 

	version("2.0.4", md5="8ef0ef685f3280527ae57d5811006a82")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-egret@3.0.5:", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
