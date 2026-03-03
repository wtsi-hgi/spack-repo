# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSleekts(RPackage):
	"""4253H, Twice Smoothing

	Compute Time series Resistant Smooth 4253H, twice smoothing method.
	"""
	
	cran = "sleekts" 

	version("1.0.2", md5="59051f16700e8cda3808909eb6dcd0d9")

	depends_on("r@3.2:", type=("build", "run"))
