# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasydb(RPackage):
	"""Easily Connect to Common Types of Databases

	A unified interface for connecting to databases ('SQLite', 'MySQL', 'PostgreSQL').
    Just provide the database name and the package will ask you questions
    to help you configure the connection and setup your credentials.  Once
    database configuration and connection has been set up once, you won't
    have to do it ever again.
	"""
	
	homepage = "https://github.com/selkamand/easydb"
	cran = "easydb" 

	version("1.1.0", md5="92fb152198456afe72835d69690b0aef")

	depends_on("r-askpass", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-keyring", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
