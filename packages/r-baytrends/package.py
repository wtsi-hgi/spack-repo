# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBaytrends(RPackage):
	"""Long Term Water Quality Trend Analysis

	Enable users to evaluate long-term trends using a Generalized 
    Additive Modeling (GAM) approach. The model development includes selecting a 
    GAM structure to describe nonlinear seasonally-varying changes over time, 
    incorporation of hydrologic variability via either a river flow or salinity, 
    the use of an intervention to deal with method or laboratory changes 
    suspected to impact data values, and representation of left- and 
    interval-censored data. The approach has been applied to water quality data 
    in the Chesapeake Bay, a major estuary on the east coast of the United 
    States to provide insights to a range of management- and research-focused 
    questions.  Methodology described in Murphy (2019) 
    <doi:10.1016/j.envsoft.2019.03.027>.
	"""
	
	homepage = "https://github.com/tetratech/baytrends"
	cran = "baytrends" 

	version("2.0.11", md5="7bfb2fb25bf4ac60ca3312579c0fc6de")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dataretrieval", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-sessioninfo", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
