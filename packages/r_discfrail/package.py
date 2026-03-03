# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscfrail(RPackage):
	"""Cox Models for Time-to-Event Data with Nonparametric Discrete
Group-Specific Frailties

	Functions for fitting Cox proportional hazards models for grouped time-to-event data, where the shared group-specific frailties have a discrete nonparametric distribution. The methods proposed in the package is described by Gasperoni, F., Ieva, F., Paganoni, A. M., Jackson, C. H., Sharples, L. (2018) <doi:10.1093/biostatistics/kxy071>. There are also functions for simulating from these models, with a nonparametric or a parametric baseline hazard function.
	"""
	
	homepage = "https://github.com/fgaspe04/discfrail"
	cran = "discfrail" 

	version("0.1", md5="c7ebb0af4a2385e5d6734611500d75a9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
