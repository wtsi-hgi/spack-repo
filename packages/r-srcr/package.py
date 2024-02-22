# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSrcr(RPackage):
	"""Simplify Connections to Database Sources

	Connecting to databases requires boilerplate code to specify
    connection parameters and to set up sessions properly with the DBMS.
    This package provides a simple tool to fill two purposes: abstracting
    connection details, including secret credentials, out of your source
    code and managing configuration for frequently-used database connections
    in a persistent and flexible way, while minimizing requirements on the
    runtime environment.
	"""
	
	cran = "srcr" 

	version("1.1.0", md5="ead97c736210b870a2f6b63217fdbb81")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
