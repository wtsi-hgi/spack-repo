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

	version("1.5-0", md5="f9b0abc412118851dc893511b0c7cc54")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-emulator", type=("build", "run"))
