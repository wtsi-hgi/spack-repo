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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/debCAM_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/debCAM/debCAM_1.20.0.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="6791c0e29dcd9dfb3c4c831b074bf34ebb4557fcce6343301651d8c869c698eb")

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
