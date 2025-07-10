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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/HD2013SGI_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/HD2013SGI/HD2013SGI_1.42.0.tar.gz"]

	version("1.42.0", sha256="a842e4015419d763d5c075aa0340eef3f1713bc06406994f901da7405541acf7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-geneplotter", type=("build", "run"))
	depends_on("r-splots", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-lsd", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))

