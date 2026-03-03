# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhm(RPackage):
	"""Phrase Mining

	Functions to extract and handle commonly occurring principal phrases
    obtained from collections of texts.
	"""
	
	cran = "phm" 

	version("1.1.2", md5="af57ef20d07df0463031ea26f5d6bb79")

	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-tm@0.7.8:", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-matrix@1.4.1:", type=("build", "run"))
	depends_on("r-smallstuff@1.0.1:", type=("build", "run"))
	depends_on("r-nlp@0.2.1:", type=("build", "run"))
