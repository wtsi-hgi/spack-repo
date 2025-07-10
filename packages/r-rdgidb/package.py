# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdgidb(RPackage):
	"""R Wrapper for DGIdb

	The rDGIdb package provides a wrapper for the Drug Gene Interaction Database (DGIdb). For simplicity, the wrapper query function and output resembles the user interface and results format provided on the DGIdb website (https://www.dgidb.org/).
	"""
	
	bioc = "rDGIdb" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rDGIdb_1.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rDGIdb/rDGIdb_1.28.0.tar.gz"]

	version("1.28.0", sha256="8c5957cbc6911c143f826dc14ed5d0ac2e6cdccd1cec214782ec791e84b38bbc")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
