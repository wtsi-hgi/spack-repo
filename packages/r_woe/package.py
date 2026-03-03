# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWoe(RPackage):
	"""Computes Weight of Evidence and Information Values

	Shows the relationship between an independent and dependent variable through Weight of Evidence and Information Value.
	"""
	
	cran = "woe" 

	version("0.2", md5="20a0ece13f62a21a24a6bbd3d3bf4465")

	depends_on("r@3.1:", type=("build", "run"))
