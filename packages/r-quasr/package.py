# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuasr(RPackage):
	"""Quantify and Annotate Short Reads in R

	This package provides a framework for the quantification and analysis of Short Reads. It covers a complete workflow starting from raw sequence reads, over creation of alignments and quality control plots, to the quantification of genomic regions of interest.
	"""
	
	bioc = "QuasR"

	version("1.48.1", commit="412e16217aa669996ca19b272e0680c410768a60")
	version("1.42.1", commit="04c840632eaa0ecc8b7e14dc349cf57a69992280")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rbowtie", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rsamtools@2.13.1:", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicfiles", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rhtslib@1.99.1:", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
