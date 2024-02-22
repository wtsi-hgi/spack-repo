# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbic(RPackage):
	"""Computing the Singular BIC for Multiple Models

	Computes the sBIC for various singular model collections including:
    binomial mixtures, factor analysis models, Gaussian mixtures,
    latent forests, latent class analyses, and reduced rank regressions.
	"""
	
	homepage = "https://github.com/Lucaweihs/sBIC"
	cran = "sBIC" 

	version("0.2.0", md5="c395934ef17b53cd69ba7f1e0e785052")

	depends_on("r-polca", type=("build", "run"))
	depends_on("r-r-oo@1.20:", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-combinat", type=("build", "run"))
	depends_on("r-flexmix", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
