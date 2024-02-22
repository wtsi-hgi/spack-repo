# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDendrotools(RPackage):
	"""Linear and Nonlinear Methods for Analyzing Daily and Monthly
Dendroclimatological Data

	Provides novel dendroclimatological methods, primarily used by the
    Tree-ring research community. There are four core functions. The first one is 
    daily_response(), which finds the optimal sequence of days that are related 
    to one or more tree-ring proxy records. Similar function is daily_response_seascorr(), 
    which implements partial correlations in the analysis of daily response functions.
    For the enthusiast of monthly data, there is monthly_response() function.
    The last core function is compare_methods(), which effectively compares several 
    linear and nonlinear regression algorithms on the task of climate reconstruction.   
	"""
	
	homepage = "https://github.com/jernejjevsenak/dendroTools"
	cran = "dendroTools" 

	version("1.2.11", md5="a0236c78867b95c92c9b5008c658004f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-brnn@0.6:", type=("build", "run"))
	depends_on("r-reshape2@1.4.2:", type=("build", "run"))
	depends_on("r-scales@0.4.1:", type=("build", "run"))
	depends_on("r-oce@1.2.0:", type=("build", "run"))
	depends_on("r-mlmetrics@1.1.1:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-knitr@1.19:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-plotly@4.7.1:", type=("build", "run"))
	depends_on("r-randomforest@4.6.14:", type=("build", "run"))
	depends_on("r-cubist@0.2.2:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-psych@1.8.3.3:", type=("build", "run"))
	depends_on("r-boot@1.3.22:", type=("build", "run"))
	depends_on("r-viridis@0.5.1:", type=("build", "run"))
	depends_on("r-dplr@1.7.2:", type=("build", "run"))
