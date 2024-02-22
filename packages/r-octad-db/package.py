# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROctadDb(RPackage):
	"""Open Cancer TherApeutic Discovery (OCTAD) database

	Open Cancer TherApeutic Discovery (OCTAD) package implies sRGES approach for the drug discovery. The essential idea is to identify drugs that reverse the gene expression signature of a disease by tamping down over-expressed genes and stimulating weakly expressed ones. The following package contains all required precomputed data for whole OCTAD pipeline computation.
	"""
	
	bioc = "octad.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/octad.db_1.4.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/octad.db/octad.db_1.4.0.tar.gz"]

	version("1.4.0", md5="ef8723031fea32015ee26dbf30d2c8ba")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))

	# experiment