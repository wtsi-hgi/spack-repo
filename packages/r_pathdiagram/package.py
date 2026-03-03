# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathdiagram(RPackage):
	"""Basic Functions for Drawing Path Diagrams

	Implementation of simple functions to draw
    basic path diagrams just for visualization purposes.
	"""
	
	homepage = "http://www.gastonsanchez.com"
	cran = "pathdiagram" 

	version("0.1.9.1", md5="9c7c5fff48007c029448026719bf1b53")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
