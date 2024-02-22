# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQmrparser(RPackage):
	"""Parser Combinator in R

	Basic functions for building parsers, with an application to PC-AXIS format files.
	"""
	
	cran = "qmrparser" 

	version("0.1.6", md5="db796a000c7761e30902e58d9c4c133e")

	depends_on("r@3.4:", type=("build", "run"))
