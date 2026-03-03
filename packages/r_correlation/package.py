# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrelation(RPackage):
	"""Methods for Correlation Analysis

	Lightweight package for computing different kinds
    of correlations, such as partial correlations, Bayesian correlations,
    multilevel correlations, polychoric correlations, biweight
    correlations, distance correlations and more. Part of the 'easystats'
    ecosystem. References: Makowski et al. (2020) <doi:10.21105/joss.02306>.
	"""
	
	homepage = "https://easystats.github.io/correlation/"
	cran = "correlation" 

	version("0.8.4", md5="f61a555cfa43c9a73466f118abadea2d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bayestestr@0.13:", type=("build", "run"))
	depends_on("r-datawizard@0.7:", type=("build", "run"))
	depends_on("r-insight@0.19.1:", type=("build", "run"))
	depends_on("r-parameters@0.20.2:", type=("build", "run"))
