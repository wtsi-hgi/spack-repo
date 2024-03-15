# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrivernet(RPackage):
	"""Drivernet: uncovering somatic driver mutations modulating transcriptional networks in cancer

	DriverNet is a package to predict functional important driver genes in cancer by integrating genome data (mutation and copy number variation data) and transcriptome data (gene expression data). The different kinds of data are combined by an influence graph, which is a gene-gene interaction network deduced from pathway data. A greedy algorithm is used to find the possible driver genes, which may mutated in a larger number of patients and these mutations will push the gene expression values of the connected genes to some extreme values.
	"""
	
	bioc = "DriverNet" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/DriverNet_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/DriverNet/DriverNet_1.42.0.tar.gz"]

	version("1.42.0", md5="78b923b016f6bd8097c1edc43ca0cca4")

	depends_on("r@2.10:", type=("build", "run"))
