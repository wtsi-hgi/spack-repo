# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLca(RPackage):
	"""Localised Co-Dependency Analysis

	Performs model fitting and significance estimation for Localised Co-Dependency between pairs of features of a numeric dataset.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "LCA" 

	version("0.1.1", md5="f297f98e930961a17b094b8cfad24f10")

	depends_on("r@2.15:", type=("build", "run"))
