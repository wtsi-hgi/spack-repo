# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAberrance(RPackage):
	"""Detect Aberrant Behavior in Test Data

	Detect several types of aberrant behavior, including answer
    copying, answer similarity, nonparametric misfit, parametric misfit,
    preknowledge, rapid guessing, and test tampering.
	"""
	
	homepage = "https://github.com/kyliegorney/aberrance"
	cran = "aberrance" 

	version("0.1.0", md5="b7e95f7cbde7e6e45bd93eb59287b4de")

	depends_on("r-mass", type=("build", "run"))
