# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbx(RPackage):
	"""A Fast, Easy-to-Use Database Interface

	Provides select, insert, update, upsert, and delete database operations. Supports 'PostgreSQL', 'MySQL', 'SQLite', and more, and plays nicely with the 'DBI' package.
	"""
	
	homepage = "https://github.com/ankane/dbx"
	cran = "dbx" 

	version("0.3.1", md5="e655065be55517ab091b681048d6e1cd")

	depends_on("r-dbi@1:", type=("build", "run"))
