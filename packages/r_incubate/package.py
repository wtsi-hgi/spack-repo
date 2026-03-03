# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncubate(RPackage):
	"""Parametric Time-to-Event Analysis with Variable Incubation
Phases

	Fit parametric models for time-to-event data that show an initial
    'incubation period', i.e., a variable delay phase where the hazard is zero. The
    delayed Weibull distribution serves as foundational data model. The
    specific method of 'MPSE' (maximum product of spacings estimation) is used for parameter
    estimation. Bootstrap confidence intervals for parameters and significance
    tests in a two group setting are provided.
	"""
	
	homepage = "https://gitlab.com/imb-dev/incubate/"
	cran = "incubate" 

	version("1.2.1", md5="5888513ae55e4cdf3c588e55a697f9ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-future@1.21:", type=("build", "run"))
	depends_on("r-future-apply@1.6:", type=("build", "run"))
	depends_on("r-glue@1.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
