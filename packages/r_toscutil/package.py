# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RToscutil(RPackage):
	"""Utility Functions

	Base R sometimes requires verbose statements for simple,
    often recurring tasks, such as printing text without trailing
    space, ending with newline. This package aims at providing
    shorthands for such tasks.
	"""
	
	homepage = "https://toscm.github.io/toscutil/"
	cran = "toscutil" 

	version("2.7.4", md5="c759e91e47e80bf4acd642273f7de667")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-languageserver", type=("build", "run"))
