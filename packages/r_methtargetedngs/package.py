# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethtargetedngs(RPackage):
	"""Perform Methylation Analysis on Next Generation Sequencing Data

	Perform step by step methylation analysis of Next Generation Sequencing data.
	"""
	
	bioc = "MethTargetedNGS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MethTargetedNGS_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MethTargetedNGS/MethTargetedNGS_1.34.0.tar.gz"]

	version("1.34.0", md5="0bce9edc9682a9ca23653409301d7225")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("hmmer@3:", type=("build", "link", "run"))
