# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRodbcdbi(RPackage):
	"""Provides Access to Databases Through the ODBC Interface

	An implementation of R's DBI interface using ODBC package as a
    back-end. This allows R to connect to any DBMS that has a ODBC driver.
	"""
	
	cran = "RODBCDBI" 

	version("0.1.1", md5="442c84cb4a4f4b9631635d12cb18f565")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rodbc", type=("build", "run"))
