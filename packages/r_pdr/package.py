# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdr(RPackage):
	"""Threshold Model and Unit Root Tests in Cross-Section and Time
Series Data

	Threshold model, panel version of Hylleberg et al. (1990) <DOI:10.1016/0304-4076(90)90080-D> seasonal unit root tests, and panel unit root test of Chang (2002) <DOI:10.1016/S0304-4076(02)00095-7>.
	"""
	
	cran = "pdR" 

	version("1.9.1", md5="722c23df94af08b86e84fdb18c22d097")

	depends_on("r@3.5:", type=("build", "run"))
