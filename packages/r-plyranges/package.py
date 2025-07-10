# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlyranges(RPackage):
	"""A fluent interface for manipulating GenomicRanges

	A dplyr-like interface for interacting with the common Bioconductor classes Ranges and GenomicRanges. By providing a grammatical and consistent way of manipulating these classes their accessiblity for new Bioconductor users is hopefully increased.
	"""
	
	bioc = "plyranges" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/plyranges_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/plyranges/plyranges_1.22.0.tar.gz"]

	version("1.22.0", sha256="fcdcad1082fadd1a365dd2d2cc7d955601b737ecd4a567d888d2b445756297fc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-iranges@2.12:", type=("build", "run"))
	depends_on("r-genomicranges@1.28.4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
