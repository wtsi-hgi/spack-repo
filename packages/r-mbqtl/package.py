# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbqtl(RPackage):
	"""mbQTL: A package for SNP-Taxa mGWAS analysis

	mbQTL is a statistical R package for simultaneous 16srRNA,16srDNA (microbial) and variant, SNP, SNV (host) relationship, correlation, regression studies. We apply linear, logistic and correlation based statistics to identify the relationships of taxa, genus, species and variant, SNP, SNV in the infected host. We produce various statistical significance measures such as P values, FDR, BC and probability estimation to show significance of these relationships. Further we provide various visualization function for ease and clarification of the results of these analysis. The package is compatible with dataframe, MRexperiment and text formats.
	"""
	
	homepage = "https://github.com/Mercedeh66/mbQTL"
	bioc = "mbQTL"

	version("1.8.0", commit="226f80d5ec98dfe3674a217b054dcb3e5a770a91")
	version("1.2.0", commit="c8ee64bd0b86af0adba9330c52590b74fed7996e")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-matrixeqtl", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-metagenomeseq", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
