# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilehashsqlite(RPackage):
	"""Simple Key-Value Database Using SQLite

	Simple key-value database using SQLite as the back end.
	"""
	
	homepage = "https://github.com/rdpeng/filehashsqlite"
	cran = "filehashSQLite" 

	version("0.2-6", md5="2d1df40715d0eabcd089e52bad49c495")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-filehash", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
