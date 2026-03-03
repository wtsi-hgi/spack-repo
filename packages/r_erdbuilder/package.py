# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErdbuilder(RPackage):
	"""Entity Relationship Diagrams Builder

	Build entity relationship diagrams (ERD) to specify the nature of the relationship between tables in a database.
	"""
	
	homepage = "https://github.com/gbasulto/ERDbuilder"
	cran = "ERDbuilder" 

	version("1.0.0", md5="2baa310059b553b392de806426c58133")

	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
