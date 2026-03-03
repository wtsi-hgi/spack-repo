# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamcopula(RPackage):
	"""Generalized Additive Models for Bivariate Conditional Dependence
Structures and Vine Copulas

	Implementation of various inference and simulation tools to
    apply generalized additive models to bivariate dependence structures and
    non-simplified vine copulas.
	"""
	
	homepage = "https://github.com/tvatter/gamCopula"
	cran = "gamCopula" 

	version("0.0-7", md5="c2f2a12f844da129edbfbc6afa9bae38")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-vinecopula@2:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-igraph@1:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
