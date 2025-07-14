# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalyzerde(RPackage):
	"""Evaluation of normalization methods and calculation of differential expression analysis statistics

	NormalyzerDE provides screening of normalization methods for LC-MS based expression data. It calculates a range of normalized matrices using both existing approaches and a novel time-segmented approach, calculates performance measures and generates an evaluation report. Furthermore, it provides an easy utility for Limma- or ANOVA- based differential expression analysis.
	"""
	
	homepage = "https://github.com/ComputationalProteomics/NormalyzerDE"
	bioc = "NormalyzerDE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/NormalyzerDE_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/NormalyzerDE/NormalyzerDE_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="425b8f99063610e9a2d1d9f362921359a5ca50244c410d6ae83d58bb634cf5b1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-vsn", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
