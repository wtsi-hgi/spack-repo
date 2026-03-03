# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSonar(RPackage):
	"""Fundamental Formulas for Sonar

	Formulas for calculating sound velocity, water pressure, depth, 
    density, absorption and sonar equations.
	"""
	
	cran = "sonar" 

	version("1.0.2", md5="03a9abd978125d7ab514fbaebeb98025")

	depends_on("r@2.7:", type=("build", "run"))
