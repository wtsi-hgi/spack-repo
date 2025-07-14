# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHd2013sgi(RPackage):
	"""Mapping genetic interactions in human cancer cells with RNAi and multiparametric phenotyping

	This package contains the experimental data and a complete executable transcript (vignette) of the analysis of the HCT116 genetic interaction matrix presented in the paper "Mapping genetic interactions in human cancer cells with RNAi and multiparametric phenotyping" by C. Laufer, B. Fischer, M. Billmann, W. Huber, M. Boutros; Nature Methods (2013) 10:427-31. doi: 10.1038/nmeth.2436.
	"""
	
	bioc = "HD2013SGI"

	version("1.48.0", commit="3a8743c27e4766c74d5c95af1a77e457d4eb2eb2")
	version("1.42.0", commit="4d9ba1fd4f7277b3fc9ddfcf0951e3530d5cd3cd")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-splots", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-lsd", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))

