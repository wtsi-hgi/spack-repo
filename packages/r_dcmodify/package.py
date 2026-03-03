# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDcmodify(RPackage):
	"""Modify Data Using Externally Defined Modification Rules

	Data cleaning scripts typically contain a lot of 'if this change that'
    type of statements. Such statements are typically condensed expert knowledge.
    With this package, such 'data modifying rules' are taken out of the code and
    become in stead parameters to the work flow. This allows one to maintain, document,
    and reason about data modification rules as separate entities.
	"""
	
	homepage = "https://github.com/data-cleaning/dcmodify"
	cran = "dcmodify" 

	version("0.9.0", md5="c72bf01f77bc91f8107df6a8748c5445")
	version("0.8.0", md5="87f9591bab61a8907d3d9e3ccc96d6b5")

	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-validate@1.1.3:", type=("build", "run"))
	depends_on("r-lumberjack@1.3.1:", type=("build", "run"))
	depends_on("r-settings", type=("build", "run"))
