# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoffda(RPackage):
	"""Goodness-of-Fit Tests for Functional Data

	Implementation of several goodness-of-fit tests for functional
    data. Currently, mostly related with the functional linear model with
    functional/scalar response and functional/scalar predictor. The package
    allows for the replication of the data applications considered in
    García-Portugués, Álvarez-Liébana, Álvarez-Pérez and González-Manteiga
    (2021) <doi:10.1111/sjos.12486>.
	"""
	
	homepage = "https://github.com/egarpor/goffda"
	cran = "goffda" 

	version("0.1.2", md5="4a6eff1f5c9e6fe87711d1a3489c35af")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fda-usc", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
