# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBnnsurvival(RPackage):
	"""Bagged k-Nearest Neighbors Survival Prediction

	Implements a bootstrap aggregated (bagged) version of
    the k-nearest neighbors survival probability prediction method (Lowsky et
    al. 2013). In addition to the bootstrapping of training samples, the
    features can be subsampled in each baselearner to break the correlation
    between them. The Rcpp package is used to speed up the computation.
	"""
	
	cran = "bnnSurvival" 

	version("0.1.5", md5="39de8061fc5498cdbb9fd9909be74440")

	depends_on("r-prodlim", type=("build", "run"))
	depends_on("r-pec", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
