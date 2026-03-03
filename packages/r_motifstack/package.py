# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifstack(RPackage):
	"""Plot stacked logos for single or multiple DNA, RNA and amino acid sequence

	The motifStack package is designed for graphic representation of multiple motifs with different similarity scores. It works with both DNA/RNA sequence motif and amino acid sequence motif. In addition, it provides the flexibility for users to customize the graphic parameters such as the font type and symbol colors.
	"""
	
	bioc = "motifStack" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/motifStack_1.46.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/motifStack/motifStack_1.46.0.tar.gz"]

	version("1.46.0", md5="b3306b32c8722e6d63ee1a37165a572e")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-ade4", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
