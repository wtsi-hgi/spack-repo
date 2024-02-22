# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConformalbayes(RPackage):
	"""Jackknife(+) Predictive Intervals for Bayesian Models

	Provides functions to construct finite-sample calibrated predictive 
    intervals for Bayesian models, following the approach in Barber et al. 
    (2021) <doi:10.1214/20-AOS1965>. These intervals are calculated efficiently
    using importance sampling for the leave-one-out residuals. By default,
    the intervals will also reflect the relative uncertainty in the Bayesian 
    model, using the locally-weighted conformal methods of Lei et al. (2018)
    <doi:10.1080/01621459.2017.1307116>.
	"""
	
	homepage = "https://github.com/CoryMcCartan/conformalbayes"
	cran = "conformalbayes" 

	version("0.1.2", md5="582700e553cd60b39636f0574306ef32")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-rstantools", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
