# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSumr(RPackage):
	"""Approximate Summation of Series

	Application of theoretical results which ensure that the summation
  of an infinite discrete series is within an arbitrary margin of error of its
  true value. The C code under the hood is shared through header files to allow
  users to sum their own low level functions as well. Based on the paper by
  Braden (1992) <doi: 10.2307/2324995>.
	"""
	
	cran = "sumR" 

	version("0.4.15", md5="5ddccde0f7b9640f944075959b966321")

	depends_on("r-matrixstats", type=("build", "run"))
