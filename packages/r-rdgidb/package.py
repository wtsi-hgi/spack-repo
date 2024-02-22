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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rDGIdb_1.28.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rDGIdb/rDGIdb_1.28.0.tar.gz"]

	version("1.28.0", md5="5f3f78a4035bbb5597811f38c68b8e4f")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
