# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZfa(RPackage):
	"""Zoom-Focus Algorithm

	Performs Zoom-Focus Algorithm (ZFA) to optimize testing regions for rare variant association tests in exome sequencing data.
	"""
	
	cran = "zfa" 

	version("1.1.0", md5="928961e687e44f67a6db6a7fb7a0fb64")

	depends_on("r-skat@1.1.2:", type=("build", "run"))
