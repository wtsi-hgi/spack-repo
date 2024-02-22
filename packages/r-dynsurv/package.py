# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynsurv(RPackage):
	"""Dynamic Models for Survival Data

	Time-varying coefficient models for interval censored and
    right censored survival data including
    1) Bayesian Cox model with time-independent, time-varying or
    dynamic coefficients for right censored and interval censored data studied by
    Sinha et al. (1999) <doi:10.1111/j.0006-341X.1999.00585.x> and
    Wang et al. (2013) <doi:10.1007/s10985-013-9246-8>,
    2) Spline based time-varying coefficient Cox model for right censored data
    proposed by Perperoglou et al. (2006) <doi:10.1016/j.cmpb.2005.11.006>, and
    3) Transformation model with time-varying coefficients for right censored data
    using estimating equations proposed by
    Peng and Huang (2007) <doi:10.1093/biomet/asm058>.
	"""
	
	homepage = "https://github.com/wenjie2wang/dynsurv"
	cran = "dynsurv" 

	version("0.4-6", md5="ee74166dc3f32a4969e19cc8f5bfd7b8")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-splines2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-bh@1.54.0.2:", type=("build", "run"))
