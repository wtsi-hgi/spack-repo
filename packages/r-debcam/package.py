# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebcam(RPackage):
	"""Deconvolution by Convex Analysis of Mixtures

	An R package for fully unsupervised deconvolution of complex tissues. It provides basic functions to perform unsupervised deconvolution on mixture expression profiles by Convex Analysis of Mixtures (CAM) and some auxiliary functions to help understand the subpopulation-specific results. It also implements functions to perform supervised deconvolution based on prior knowledge of molecular markers, S matrix or A matrix. Combining molecular markers from CAM and from prior knowledge can achieve semi-supervised deconvolution of mixtures.
	"""
	
	bioc = "debCAM"

	version("1.26.0", commit="32c218e8f707d067737147257bc8824797842f6e")
	version("1.20.0", commit="6ad0999b13d1209d732f3b9ef8d99dc4c89c5ef0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-dmwr2", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-apcluster", type=("build", "run"))
	depends_on("openjdk@1.8:", type=("build", "link", "run"))
