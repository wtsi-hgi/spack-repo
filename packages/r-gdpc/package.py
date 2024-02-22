# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdpc(RPackage):
	"""Generalized Dynamic Principal Components

	Functions to compute the Generalized Dynamic Principal Components
    introduced in Peña and Yohai (2016) <DOI:10.1080/01621459.2015.1072542>. The implementation
    includes an automatic procedure proposed in Peña, Smucler and Yohai (2020) <DOI:10.18637/jss.v092.c02>
    for the identification of both the number of lags to be used
    in the generalized dynamic principal components as well as the number of components required
    for a given reconstruction accuracy.
	"""
	
	cran = "gdpc" 

	version("1.1.4", md5="cf4841aa0cac7b9a7c79e183a0b7dfea")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.500:", type=("build", "run"))
