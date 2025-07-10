# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmadb(RPackage):
	"""R wrapper for the OMA REST API

	A package for the orthology prediction data download from OMA database.
	"""
	
	homepage = "https://github.com/DessimozLab/OmaDB"
	bioc = "OmaDB" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/OmaDB_2.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/OmaDB/OmaDB_2.18.0.tar.gz"]

	version("2.18.0", sha256="e7b14fdbd507a7c189fd9a84aa027533fbf10d92bbee2275ef76604b5245fed9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr@1.2.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-ape", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
