# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpivizr(RPackage):
	"""R Interface to epiviz web app

	This package provides connections to the epiviz web app (http://epiviz.cbcb.umd.edu) for interactive visualization of genomic data. Objects in R/bioc interactive sessions can be displayed in genome browser tracks or plots to be explored by navigation through genomic regions. Fundamental Bioconductor data structures are supported (e.g., GenomicRanges and RangedSummarizedExperiment objects), while providing an easy mechanism to support other data structures (through package epivizrData). Visualizations (using d3.js) can be easily added to the web app as well.
	"""
	
	bioc = "epivizr" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epivizr_2.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epivizr/epivizr_2.32.0.tar.gz"]

    version("2.38.0", tag="RELEASE_3_21")
	version("2.32.0", sha256="3217a45762f882999006c05e21a3a3fe444c19cbfaea447f90c5db7180347124")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-epivizrserver@1.1.1:", type=("build", "run"))
	depends_on("r-epivizrdata@1.3.4:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-bumphunter", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
