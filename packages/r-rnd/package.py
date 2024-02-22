# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnd(RPackage):
	"""Risk Neutral Density Extraction Package

	Extract the implied risk neutral density from options using various methods.
	"""
	
	cran = "RND" 

	version("1.2", md5="8a29d48702d136b5782c72ceaa691a75")

	depends_on("r@3.0.1:", type=("build", "run"))
