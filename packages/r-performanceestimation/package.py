# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerformanceestimation(RPackage):
	"""An Infra-Structure for Performance Estimation of Predictive
Models

	An infra-structure for estimating the predictive performance of
    predictive models. In this context, it can also be used to compare and/or select
    among different alternative ways of solving one or more predictive tasks. The
    main goal of the package is to provide a generic infra-structure to estimate
    the values of different metrics of predictive performance using different
    estimation procedures. These estimation tasks can be applied to any solutions
    (workflows) to the predictive tasks. The package provides easy to use standard
    workflows that allow the usage of any available R modeling algorithm together
    with some pre-defined data pre-processing steps and also prediction post-
    processing methods. It also provides means for addressing issues related with
    the statistical significance of the observed differences.
	"""
	
	homepage = "https://github.com/ltorgo/performanceEstimation"
	cran = "performanceEstimation" 

	version("1.1.0", md5="1a4ab4ef10d42d50472eba8ed88a2527")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@0.9.3:", type=("build", "run"))
	depends_on("r-parallelmap@1.3:", type=("build", "run"))
	depends_on("r-tidyr@0.4.1:", type=("build", "run"))
	depends_on("r-dplyr@0.4.3:", type=("build", "run"))
