# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRjdbc(RPackage):
	"""Provides Access to Databases Through the JDBC Interface

	The RJDBC package is an implementation of R's DBI interface using JDBC as a back-end. This allows R to connect to any DBMS that has a JDBC driver.
	"""
	
	homepage = "http://www.rforge.net/RJDBC/"
	cran = "RJDBC" 

	version("0.2-10", md5="a7f309b83acc1d3cdfb2a5914023cab7")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rjava@0.4.15:", type=("build", "run"))
	depends_on("r@2.4:", type=("build", "run"))
