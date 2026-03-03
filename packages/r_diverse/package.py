# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiverse(RPackage):
	"""Diversity Measures for Complex Systems

	Computes the most common diversity measures used in social and other sciences, and includes new measures from interdisciplinary research.
	"""
	
	homepage = "https://github.com/mguevara/diverse"
	cran = "diverse" 

	version("0.1.5", md5="a9ee969a658c77a79e92867f8a43829e")

	depends_on("r-proxy", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
