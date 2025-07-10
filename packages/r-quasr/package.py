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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/QuasR_1.42.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/QuasR/QuasR_1.42.1.tar.gz"]

	version("1.42.1", sha256="d66ef1bbf95ae60bb5b7cf87dea6dae6adcc92229ef69984b1589073b7bc2519")

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
