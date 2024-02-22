# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForams(RPackage):
	"""Foraminifera and Community Ecology Analyses

	SHE, FORAM Index and ABC Method analyses and custom plot
        functions for community data.
	"""
	
	cran = "forams" 

	version("2.0-6", md5="f14d27675ad72ae2058ff790a6a541e3")

	depends_on("r-vegan", type=("build", "run"))
