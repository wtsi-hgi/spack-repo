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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tRNAscanImport_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tRNAscanImport/tRNAscanImport_1.22.0.tar.gz"]

	version("1.22.0", md5="49f872c7de9b6cba139c7758330efa8c")

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
