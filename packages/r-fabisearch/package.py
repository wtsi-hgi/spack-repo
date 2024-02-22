# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabisearch(RPackage):
	"""Change Point Detection in High-Dimensional Time Series Networks

	Implementation of the Factorized Binary Search (FaBiSearch) methodology for the estimation of the number and the location of multiple change points in the network (or clustering) structure of multivariate high-dimensional time series. The method is motivated by the detection of change points in functional connectivity networks for functional magnetic resonance imaging (fMRI) data. FaBiSearch uses non-negative matrix factorization (NMF), an unsupervised dimension reduction technique, and a new binary search algorithm to identify multiple change points.  It requires minimal assumptions. Lastly, we provide interactive, 3-dimensional, brain-specific network visualization capability in a flexible, stand-alone function. This function can be conveniently used with any node coordinate atlas, and nodes can be color coded according to community membership, if applicable. The output is an elegantly displayed network laid over a cortical surface, which can be rotated in the 3-dimensional space. The main routines of the package are detect.cps(), for multiple change point detection, est.net(), for estimating a network between stationary multivariate time series, net.3dplot(), for plotting the estimated functional connectivity networks, and opt.rank(), for finding the optimal rank in NMF for a given data set. The functions have been extensively tested on simulated multivariate high-dimensional time series data and fMRI data. For details on the FaBiSearch methodology, please see Ondrus et al. (2021) <arXiv:2103.06347>. For a more detailed explanation and applied examples of the fabisearch package, please see Ondrus and Cribben (2022), preprint.
	"""
	
	homepage = "https://github.com/mondrus96/FaBiSearch"
	cran = "fabisearch" 

	version("0.0.4.5", md5="835bd32cddc4955fd8d739cd39af3f7f")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
