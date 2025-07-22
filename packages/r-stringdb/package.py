# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStringdb(RPackage):
	"""STRINGdb - Protein-Protein Interaction Networks and Functional Enrichment Analysis

	The STRINGdb package provides a R interface to the STRING protein-protein interactions database (https://string-db.org).
	"""
	
	bioc = "STRINGdb" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/STRINGdb_2.14.3.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/STRINGdb/STRINGdb_2.14.3.tar.gz"]

    version("2.20.0", tag="RELEASE_3_21")
	version("2.14.3", sha256="7052094c9a4dd8f60e9bb0dd1d68cab305568cd8e3dec5beba3a8bf7d99f6c19")
	version("2.14.0", md5="6dc5819519574f0656e4b811e4618db7")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-hash", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
