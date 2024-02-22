# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMssql(RPackage):
	"""Tools to Work with Microsoft SQL Server Databases via 'RODBC'

	Tools that extend the functionality of the 'RODBC' package to work
  with Microsoft SQL Server databases. Makes it easier to browse the database
  and examine individual tables and views.
	"""
	
	cran = "MSSQL" 

	version("1.0.0", md5="889f64f3dad2716de0982d2d30dbd594")

	depends_on("r-rodbc", type=("build", "run"))
