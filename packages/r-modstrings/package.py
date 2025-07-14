# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModstrings(RPackage):
	"""Working with modified nucleotide sequences

	Representing nucleotide modifications in a nucleotide sequence is usually done via special characters from a number of sources. This represents a challenge to work with in R and the Biostrings package. The Modstrings package implements this functionallity for RNA and DNA sequences containing modified nucleotides by translating the character internally in order to work with the infrastructure of the Biostrings package. For this the ModRNAString and ModDNAString classes and derivates and functions to construct and modify these objects despite the encoding issues are implemenented. In addition the conversion from sequences to list like location information (and the reverse operation) is implemented as well.
	"""
	
	bioc = "Modstrings"

	version("1.24.0", commit="6b597518ef1b72cf173c2bf2c4d35291580a0041")
	version("1.18.0", commit="27ebb4be3b78c7dfdd7e9fd96614fd946d771bb8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biostrings@2.51.5:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
