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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tRNAdbImport_1.20.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tRNAdbImport/tRNAdbImport_1.20.1.tar.gz"]

    version("1.26.0", tag="RELEASE_3_21")
	version("1.20.1", sha256="d15a0fd1e9fb300b8e884c9971e9cc0299391f289ff311b4979184d4ab8e55c4")

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
