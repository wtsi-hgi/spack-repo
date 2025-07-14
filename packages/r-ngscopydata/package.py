# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgscopydata(RPackage):
	"""Subset of BAM files of human tumor and pooled normal sequencing data (Zhao et al. 2014) for the NGScopy package

	Subset of BAM files of human lung tumor and pooled normal samples by targeted panel sequencing. [Zhao et al 2014. Targeted Sequencing in Non-Small Cell Lung Cancer (NSCLC) Using the University of North Carolina (UNC) Sequencing Assay Captures Most Previously Described Genetic Aberrations in NSCLC. In preparation.] Each sample is a 10 percent random subsample drawn from the original sequencing data. The pooled normal sample has been rescaled accroding to the total number of normal samples in the "pool". Here provided is the subsampled data on chr6 (hg19).
	"""
	
	bioc = "NGScopyData"

	version("1.28.0", commit="7bbf4de601c76dd241541622ea712906faba9d4a")
	version("1.22.0", commit="9d1a43d67e1beb8e3e237df164c6fe7db803c658")


