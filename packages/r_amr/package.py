# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmr(RPackage):
	"""Antimicrobial Resistance Data Analysis

	Functions to simplify and standardise antimicrobial resistance (AMR)
  data analysis and to work with microbial and antimicrobial properties by
  using evidence-based methods, as described in <doi:10.18637/jss.v104.i03>.
	"""
	
	homepage = "https://msberends.github.io/AMR/"
	cran = "AMR" 

	version("2.1.1", md5="a56df7da2d4cc47f25ad11e22d7303cf")

	depends_on("r@3:", type=("build", "run"))
