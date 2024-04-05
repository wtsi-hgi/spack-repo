# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMirnatapDb(RPackage):
	"""Data for miRNAtap

	This package holds the database for miRNAtap.
	"""
	
	bioc = "miRNAtap.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/miRNAtap.db_0.99.10.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/miRNAtap.db/miRNAtap.db_0.99.10.tar.gz"]

	version("0.99.10", md5="48010280b68d6f1ddbff3b374132ce0a")

	depends_on("r-mirnatap", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))

