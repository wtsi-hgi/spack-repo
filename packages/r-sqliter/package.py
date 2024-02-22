# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqliter(RPackage):
	"""Connection wrapper to SQLite databases

	sqliter helps users, mainly data munging practioneers, to organize
    their sql calls in a clean structure. It simplifies the process of
    extracting and transforming data into useful formats.
	"""
	
	homepage = "https://github.com/wilsonfreitas/sqliter/"
	cran = "sqliter" 

	version("0.1.0", md5="1aed0c10c10a306132d258d78c973196")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-functional", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
