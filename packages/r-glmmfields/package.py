# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmmfields(RPackage):
	"""Generalized Linear Mixed Models with Robust Random Fields for
Spatiotemporal Modeling

	Implements Bayesian spatial and spatiotemporal
    models that optionally allow for extreme spatial deviations through
    time. 'glmmfields' uses a predictive process approach with random
    fields implemented through a multivariate-t distribution instead of
    the usual multivariate normal.  Sampling is conducted with 'Stan'.
    References: Anderson and Ward (2019) <doi:10.1002/ecy.2403>.
	"""
	
	homepage = "https://github.com/seananderson/glmmfields"
	cran = "glmmfields" 

	version("0.1.8", md5="2959b8f8c5102e2cbdf02be4161e8adc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rcpp@0.12.8:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-broom-mixed", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-dplyr@0.8:", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-loo@2:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
