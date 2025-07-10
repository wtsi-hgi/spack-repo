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

	version("1.22.0", sha256="f6cf1809194c84d198e032182796abbd9c25847c9201b7193e89fc97eb30d7a3")

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
