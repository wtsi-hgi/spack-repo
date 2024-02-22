# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrnadbimport(RPackage):
	"""Importing from tRNAdb and mitotRNAdb as GRanges objects

	tRNAdbImport imports the entries of the tRNAdb and mtRNAdb (http://trna.bioinf.uni-leipzig.de) as GRanges object.
	"""
	
	bioc = "tRNAdbImport" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/tRNAdbImport_1.20.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/tRNAdbImport/tRNAdbImport_1.20.1.tar.gz"]

	version("1.20.1", md5="800f0115cf3ffcfb1fd2dd45b3574f30")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-modstrings", type=("build", "run"))
	depends_on("r-structstrings", type=("build", "run"))
	depends_on("r-trna", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
