# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdapts(RPackage):
	"""Automated Deconvolution Augmentation of Profiles for Tissue
Specific Cells

	Tools to construct (or add to) cell-type signature matrices using flow sorted or single cell samples and deconvolve bulk gene expression data.
    Useful for assessing the quality of single cell RNAseq experiments, estimating the accuracy of signature matrices, and determining cell-type spillover. 
    Please cite: Danziger SA et al. (2019) ADAPTS: Automated Deconvolution Augmentation of Profiles for Tissue Specific cells <doi:10.1371/journal.pone.0224693>.
	"""
	
	cran = "ADAPTS" 

	version("1.0.22", md5="a4eb980950940bd2eb24ddfe8fb6ffa8")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-comics", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-quantmod", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
	depends_on("r-ranger", type=("build", "run"))
