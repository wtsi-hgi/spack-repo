# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStacomirtools(RPackage):
	"""Connection Class for Package stacomiR

	S4 class wrappers for the 'ODBC' and Pool DBI connection, also provides some 
    utilities to paste small datasets to clipboard, rename columns. It is used by the package 'stacomiR' for
    connections to the database. Development versions of 'stacomiR' are available in R-forge.
	"""
	
	cran = "stacomirtools" 

	version("0.6.0.1", md5="39b51c492ef196727533781a6dfcf08f")

	depends_on("r-rodbc", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-pool", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
