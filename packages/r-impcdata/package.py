# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImpcdata(RPackage):
	"""Retrieves data from IMPC database

	Package contains methods for data retrieval from IMPC Database.
	"""
	
	bioc = "IMPCdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IMPCdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IMPCdata/IMPCdata_1.38.0.tar.gz"]

	version("1.38.0", sha256="d56bd3aa0e47be147b6160f7b69737a711da6c4ef0075c539aff1b125d499872")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
