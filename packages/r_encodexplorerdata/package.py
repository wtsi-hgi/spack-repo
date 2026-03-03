# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncodexplorerdata(RPackage):
	"""A compilation of ENCODE metadata

	This package allows user to quickly access ENCODE project files metadata and give access to helper functions to query the ENCODE rest api, download ENCODE datasets and save the database in SQLite format.
	"""
	
	bioc = "ENCODExplorerData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ENCODExplorerData_0.99.5.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ENCODExplorerData/ENCODExplorerData_0.99.5.tar.gz"]

	version("0.99.5", md5="c6d9b491548529db0739b79c98adacd7")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))

