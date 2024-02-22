# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDs(RPackage):
	"""Descriptive Statistics

	Performs various analyzes of descriptive statistics, including correlations, graphics and tables. 
	"""
	
	cran = "ds" 

	version("4.0", md5="50dc5061b85c20ecbe4d0b4b1f76ce84")

	depends_on("r@3:", type=("build", "run"))
