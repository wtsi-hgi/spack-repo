# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTress(RPackage):
	"""Toolbox for mRNA epigenetics sequencing analysis

	This package is devoted to analyzing MeRIP-seq data. Current functionalities include 1. detect transcriptome wide m6A methylation regions 2. detect transcriptome wide differential m6A methylation regions.
	"""
	
	bioc = "TRESS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/TRESS_1.8.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/TRESS/TRESS_1.8.0.tar.gz"]

	version("1.8.0", sha256="8732c8493520665430e6eb8fb2992645451343919d6897e10d35e19399729bee")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
