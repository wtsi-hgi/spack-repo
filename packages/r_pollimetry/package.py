# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPollimetry(RPackage):
	"""Estimate Pollinator Body Size and Co-Varying Ecological Traits

	Tools to estimate pollinator body size and co-varying traits. This package contains novel Bayesian predictive models of pollinator body size (for bees and hoverflies) as well as preexisting predictive models for pollinator body size (currently implemented for ants, bees, butterflies, flies, moths and wasps) as well as bee tongue length and foraging distance, total field nectar loads and wing loading. An additional GitHub repository <https://github.com/liamkendall/pollimetrydata> provides model objects to use the bodysize function internally. All models are described in Kendall et al (2018) <doi:10.1101/397604>.
	"""
	
	cran = "pollimetry" 

	version("1.0.1", md5="0152dabd8ba1c5e96d2cd68d49489e24")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-brms@2.4:", type=("build", "run"))
	depends_on("r-repmis", type=("build", "run"))
