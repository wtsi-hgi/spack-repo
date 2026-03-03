# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInters(RPackage):
	"""Flexible Tools for Estimating Interactions

	A set of functions to estimate interactions flexibly in the face of possibly many controls. Implements the procedures described in Blackwell and Olson (2022) <doi:10.1017/pan.2021.19>.
	"""
	
	homepage = "https://mattblackwell.github.io/inters/"
	cran = "inters" 

	version("0.2.0", md5="dcb0503c00cdb4b227d8165a76dc6051")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fixest", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
