# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSjdbc(RPackage):
	"""JDBC Driver Interface

	Provides a database-independent JDBC interface.
	"""
	
	cran = "sjdbc" 

	version("1.6.1", md5="2886a527ca420a13063226f62d58d322")

	depends_on("r-rjava", type=("build", "run"))
