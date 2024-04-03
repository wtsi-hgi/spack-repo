# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnion(RPackage):
	"""Octonions and Quaternions

	
  Quaternions and Octonions are four- and eight- dimensional
  extensions of the complex numbers.  They are normed division
  algebras over the real numbers and find applications in spatial
  rotations (quaternions), and string theory and relativity
  (octonions).  The quaternions are noncommutative and the octonions
  nonassociative.  See the package vignette for more details.
	"""
	
	homepage = "https://github.com/RobinHankin/onion"
	cran = "onion" 

	version("1.5-3", md5="afeafe5119bfc1f064182c37cb43ead5")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-emulator", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-freealg@1.0.4:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
