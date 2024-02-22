# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrim(RPackage):
	"""Graphical Interaction Models

	Provides the following types of models: Models for contingency
    tables (i.e. log-linear models) Graphical Gaussian models for multivariate
    normal data (i.e. covariance selection models) Mixed interaction models.
    Documentation about 'gRim' is provided by vignettes included in this
    package and the book by Højsgaard, Edwards and Lauritzen (2012,
    <doi:10.1007/978-1-4614-2299-0>); see 'citation("gRim")' for details.
	"""
	
	homepage = "https://people.math.aau.dk/~sorenh/software/gR/"
	cran = "gRim" 

	version("0.3.0", md5="3ef179bf263db5f5d13e0c9f49fce7d6")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-grbase@2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-grain@1.3.10:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcpp@0.11.1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
