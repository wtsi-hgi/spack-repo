# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSasfunclust(RPackage):
	"""Sparse and Smooth Functional Clustering

	Implements the sparse and smooth functional clustering (SaS-Funclust) method (Centofanti et al. (2021) <arXiv:2103.15224>) that aims to classify a sample of curves into homogeneous groups while jointly detecting the most informative portions of domain.
	"""
	
	homepage = "https://github.com/unina-sfere/sasfunclust"
	cran = "sasfunclust" 

	version("1.0.0", md5="2f5b233ad3324667fbc65edf8ec914d7")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
