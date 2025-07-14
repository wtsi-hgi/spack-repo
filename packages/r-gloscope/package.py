# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGloscope(RPackage):
	"""Population-level Representation on scRNA-Seq data

	This package aims at representing and summarizing the entire single-cell profile of a sample. It allows researchers to perform important bioinformatic analyses at the sample-level such as visualization and quality control. The main functions Estimate sample distribution and calculate statistical divergence among samples, and visualize the distance matrix through MDS plots.
	"""
	
	bioc = "GloScope" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GloScope_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GloScope/GloScope_1.0.0.tar.gz"]

    version("1.6.0", tag="RELEASE_3_21")
	version("1.0.0", sha256="029f7f57db10e1f0fa33ce37227a6ed2f21b1a0cd6cf02fa8e868128e60552fe")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rann", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-mvnfast", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
