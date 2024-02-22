# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpensemble(RPackage):
	"""Random Projection Ensemble Classification

	Implements the methodology of "Cannings, T. I. and Samworth, R. J. (2017) Random-projection ensemble classification, J. Roy. Statist. Soc., Ser. B. (with discussion), 79, 959--1035". The random projection ensemble classifier is a general method for classification of high-dimensional data, based on careful combination of the results of applying an arbitrary base classifier to random projections of the feature vectors into a lower-dimensional space. The random projections are divided into non-overlapping blocks, and within each block the projection yielding the smallest estimate of the test error is selected. The random projection ensemble classifier then aggregates the results of applying the base classifier on the selected projections, with a data-driven voting threshold to determine the final assignment. 
	"""
	
	homepage = "https://arxiv.org/abs/1504.04595"
	cran = "RPEnsemble" 

	version("0.5", md5="92fedaa2b3c469f393304324372c251e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
