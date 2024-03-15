# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNgscopydata(RPackage):
	"""Subset of BAM files of human tumor and pooled normal sequencing data (Zhao et al. 2014) for the NGScopy package

	Subset of BAM files of human lung tumor and pooled normal samples by targeted panel sequencing. [Zhao et al 2014. Targeted Sequencing in Non-Small Cell Lung Cancer (NSCLC) Using the University of North Carolina (UNC) Sequencing Assay Captures Most Previously Described Genetic Aberrations in NSCLC. In preparation.] Each sample is a 10 percent random subsample drawn from the original sequencing data. The pooled normal sample has been rescaled accroding to the total number of normal samples in the "pool". Here provided is the subsampled data on chr6 (hg19).
	"""
	
	homepage = "http://www.bioconductor.org/packages/release/data/experiment/html/NGScopyData.html"
	bioc = "NGScopyData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/NGScopyData_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/NGScopyData/NGScopyData_1.22.0.tar.gz"]

	version("1.22.0", md5="0ba77cf672a331e4c9dd90b26f41b5c6")


	# experiment