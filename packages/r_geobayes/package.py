# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeobayes(RPackage):
	"""Analysis of Geostatistical Data using Bayes and Empirical Bayes
Methods

	Functions to fit geostatistical data. The data can be
        continuous, binary or count data and the models implemented are
        flexible. Conjugate priors are assumed on some parameters while
        inference on the other parameters can be done through a full
        Bayesian analysis of by empirical Bayes methods.
	"""
	
	cran = "geoBayes" 

	version("0.7.3", md5="603a57af18be31745218b777c6f9d2eb")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-optimx", type=("build", "run"))
