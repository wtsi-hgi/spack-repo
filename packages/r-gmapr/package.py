# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmapr(RPackage):
	"""An R interface to the GMAP/GSNAP/GSTRUCT suite

	GSNAP and GMAP are a pair of tools to align short-read data written by Tom Wu.  This package provides convenience methods to work with GMAP and GSNAP from within R. In addition, it provides methods to tally alignment results on a per-nucleotide basis using the bam_tally tool.
	"""
	
	bioc = "gmapR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/gmapR_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/gmapR/gmapR_1.44.0.tar.gz"]

	version("1.44.0", sha256="9a4170ff62a8a5482a5f77187ec9b3791896546c1eb1038545eb7f90cf488022")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.1.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.31.8:", type=("build", "run"))
	depends_on("r-rsamtools@1.31.2:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-biocgenerics@0.25.1:", type=("build", "run"))
	depends_on("r-rtracklayer@1.39.7:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.31.3:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-variantannotation@1.25.11:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomicalignments@1.15.6:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
