# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvanumt(RPackage):
	"""NUMT detection from structural variant calls

	svaNUMT contains functions for detecting NUMT events from structural variant calls. It takes structural variant calls in GRanges of breakend notation and identifies NUMTs by nuclear-mitochondrial breakend junctions. The main function reports candidate NUMTs if there is a pair of valid insertion sites found on the nuclear genome within a certain distance threshold. The candidate NUMTs are reported by events.
	"""
	
	bioc = "svaNUMT" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/svaNUMT_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/svaNUMT/svaNUMT_1.8.0.tar.gz"]

	version("1.8.0", md5="1f25f8632f0e52d0826ee0b1b8a1fe28")

	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
	depends_on("r-structuralvariantannotation", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r@4:", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
