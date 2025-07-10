# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStructstrings(RPackage):
	"""Implementation of the dot bracket annotations with Biostrings

	The Structstrings package implements the widely used dot bracket annotation for storing base pairing information in structured RNA. Structstrings uses the infrastructure provided by the Biostrings package and derives the DotBracketString and related classes from the BString class. From these, base pair tables can be produced for in depth analysis. In addition, the loop indices of the base pairs can be retrieved as well. For better efficiency, information conversion is implemented in C, inspired to a large extend by the ViennaRNA package.
	"""
	
	homepage = "https://github.com/FelixErnst/Structstrings"
	bioc = "Structstrings" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Structstrings_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Structstrings/Structstrings_1.18.0.tar.gz"]

	version("1.18.0", sha256="b4997ef93e6388c26246b9f9c79f8cde834f467f5092ef7cb21c8c26219c4182")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings@2.57.2:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
