# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprbase(RPackage):
	"""Base functions and classes for CRISPR gRNA design

	Provides S4 classes for general nucleases, CRISPR nucleases, CRISPR nickases, and base editors.Several CRISPR-specific genome arithmetic functions are implemented to help extract genomic coordinates of spacer and protospacer sequences. Commonly-used CRISPR nuclease objects are provided that can be readily used in other packages. Both DNA- and RNA-targeting nucleases are supported.
	"""
	
	homepage = "https://github.com/crisprVerse/crisprBase"
	bioc = "crisprBase"

	version("1.12.0", commit="ecabfe9f27a75c5ac90754317805d7112debe7f6")
	version("1.6.0", commit="bee5106c4452c9749153fd95a61426aff8c84523")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
