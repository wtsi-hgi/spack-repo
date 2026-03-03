# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RD4storagehub4r(RPackage):
	"""Interface to 'D4Science' 'StorageHub' API

	Provides an interface to 'D4Science' 'StorageHub' API (<https://dev.d4science.org/>). Allows to get user profile, and perform 
 actions over the 'StorageHub' (workspace) including creation of folders, files management (upload/update/deletion/sharing), and listing of 
 stored resources.
	"""
	
	homepage = "https://github.com/eblondel/d4storagehub4R"
	cran = "d4storagehub4R" 

	version("0.4-3", md5="e6a26c00e122d306d7c06a29146e9648")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
