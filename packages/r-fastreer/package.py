# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastreer(RPackage):
	"""Phylogenetic, Distance and Other Calculations on VCF and Fasta Files

	Calculate distances, build phylogenetic trees or perform hierarchical clustering between the samples of a VCF or FASTA file. Functions are implemented in Java and called via rJava. Parallel implementation that operates directly on the VCF or FASTA file for fast execution.
	"""
	
	homepage = "https://github.com/gkanogiannis/fastreeR"
	bioc = "fastreeR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/fastreeR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/fastreeR/fastreeR_1.6.0.tar.gz"]

	version("1.6.0", md5="e2b7164aeaa305f819536d9b85e4de12")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dynamictreecut", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("openjdk@8:", type=("build", "link", "run"))
