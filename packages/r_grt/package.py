# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrt(RPackage):
	"""General Recognition Theory

	Functions to generate and analyze data for psychology experiments based on the General Recognition Theory.
	"""
	
	cran = "grt" 

	version("0.2.1", md5="1a674584570225f285b8eb18088c061a")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
