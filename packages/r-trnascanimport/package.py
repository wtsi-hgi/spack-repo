# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrnascanimport(RPackage):
	"""Importing a tRNAscan-SE result file as GRanges object

	The package imports the result of tRNAscan-SE as a GRanges object.
	"""
	
	homepage = "https://github.com/FelixErnst/tRNAscanImport"
	bioc = "tRNAscanImport"

	version("1.28.0", commit="4039806a8e0e0bcc115023ad75a6488051c7879a")
	version("1.22.0", commit="2f69582c03e699405774b272ca0f320603bac87a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-trna", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-structstrings", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
