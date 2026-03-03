# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHextri(RPackage):
	"""Hexbin Plots with Triangles

	Display hexagonally binned scatterplots for multi-class data, using coloured triangles to show class proportions.
	"""
	
	cran = "hextri" 

	version("0.9.17", md5="1283a9ffaa23a8ab187afe5a072b7549")

	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
