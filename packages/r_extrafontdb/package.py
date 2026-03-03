# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExtrafontdb(RPackage):
	"""Package for holding the database for the extrafont package

	Package for holding the database for the extrafont package
	"""
	
	homepage = "https://github.com/wch/extrafontdb"
	cran = "extrafontdb" 

	version("1.0", md5="69f3ce30cdd568e31369bdea7583943c")

	depends_on("r@2.14:", type=("build", "run"))
