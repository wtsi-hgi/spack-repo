# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBwd(RPackage):
	"""Backward Procedure for Change-Point Detection

	Implements a backward procedure for single and multiple change point detection proposed by Shin et al. <arXiv:1812.10107>. The backward approach is particularly useful to detect short and sparse signals which is common in copy number variation (CNV) detection. 
	"""
	
	cran = "bwd" 

	version("0.1.0", md5="73d213047f8b3edc0df3dcb8bad7e307")

	depends_on("r@3.4:", type=("build", "run"))
