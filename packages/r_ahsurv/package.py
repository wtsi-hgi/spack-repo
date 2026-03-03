# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAhsurv(RPackage):
	"""Flexible Parametric Accelerated Hazards Models

	Flexible parametric Accelerated Hazards (AH) regression models in overall and relative survival frameworks with 13 distinct Baseline Distributions. The AH Model can also be applied to lifetime data with crossed survival curves. Any user-defined parametric distribution can be fitted, given at least an R function defining the cumulative hazard and hazard rate functions. See Chen and Wang (2000) <doi:10.1080/01621459.2000.10474236>, and Lee (2015) <doi:10.1007/s10985-015-9349-5> for more details.
	"""
	
	cran = "AHSurv" 

	version("0.1.0", md5="45828f380a51fb822339f3683037e8ac")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-rootsolve", type=("build", "run"))
