# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdols(RPackage):
	"""Inference of Quadratic Functional for Moderate-Dimensional OLS

	Statistical inference for quadratic functional of the moderate-dimensional linear model in Guo and Cheng (2021) <DOI:10.1080/01621459.2021.1893177>.
	"""
	
	cran = "MDOLS" 

	version("1.0", md5="742ce9c16cfd618e94398505b63d2ab0")

