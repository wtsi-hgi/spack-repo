# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultibac(RPackage):
	"""Multiomic Batch effect Correction

	MultiBaC is a strategy to correct batch effects from multiomic datasets distributed across different labs or data acquisition events. MultiBaC is the first Batch effect correction algorithm that dealing with batch effect correction in multiomics datasets. MultiBaC is able to remove batch effects across different omics generated within separate batches provided that at least one common omic data type is included in all the batches considered.
	"""
	
	bioc = "MultiBaC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MultiBaC_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MultiBaC/MultiBaC_1.12.0.tar.gz"]

	version("1.12.0", md5="5585e9f823074db09f44221063a3e64b")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-ropls", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-pcamethods", type=("build", "run"))
