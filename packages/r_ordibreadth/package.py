# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdibreadth(RPackage):
	"""Ordinated Diet Breadth

	Calculates ordinated diet breadth with some plotting functions.
	"""
	
	cran = "ordiBreadth" 

	version("1.0", md5="e6b8e7dc2bf720eb118c6d78b6f13baa")

	depends_on("r-vegan", type=("build", "run"))
