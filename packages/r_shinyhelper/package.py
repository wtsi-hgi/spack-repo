# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShinyhelper(RPackage):
	"""Easily Add Markdown Help Files to 'shiny' App Elements

	Creates a lightweight way to add markdown helpfiles to 'shiny' apps,
    using modal dialog boxes, with no need to observe each help button separately.
	"""
	
	cran = "shinyhelper" 

	version("0.3.2", md5="d064472d20b781bb00fbe29f2664b0eb")

	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
