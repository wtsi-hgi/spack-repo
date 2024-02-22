# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotifmatchr(RPackage):
	"""Fast Motif Matching in R

	Quickly find motif matches for many motifs and many sequences. Wraps C++ code from the MOODS motif calling library, which was developed by Pasi Rastas, Janne Korhonen, and Petri Martinmäki.
	"""
	
	bioc = "motifmatchr" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/motifmatchr_1.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/motifmatchr/motifmatchr_1.24.0.tar.gz"]

	version("1.24.0", md5="23c63cb97f5e359a4fb9e5e6751e037d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tfbstools", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
