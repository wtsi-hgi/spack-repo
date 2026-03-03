# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRamps(RPackage):
	"""Bayesian Geostatistical Modeling with RAMPS

	Bayesian geostatistical modeling of Gaussian processes using a
    reparameterized and marginalized posterior sampling (RAMPS) algorithm
    designed to lower autocorrelation in MCMC samples.  Package performance is
    tuned for large spatial datasets.
	"""
	
	homepage = "https://www.jstatsoft.org/v25/i10"
	cran = "ramps" 

	version("0.6.18", md5="1d1a08191ca3b5366d03de621e34e668")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
