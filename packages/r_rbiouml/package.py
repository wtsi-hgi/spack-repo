# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbiouml(RPackage):
	"""Interact with BioUML Server

	Functions for connecting to BioUML server, querying BioUML repository and launching BioUML analyses.
	"""
	
	cran = "rbiouml" 

	version("1.11", md5="15c01b22fdf4f1b518fa39f5a6e95580")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
