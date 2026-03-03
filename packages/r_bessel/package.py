# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBessel(RPackage):
	"""Computations and Approximations for Bessel Functions

	Computations for Bessel function for complex, real and partly
  'mpfr' (arbitrary precision) numbers; notably interfacing TOMS 644;
  approximations for large arguments, experiments, etc.
	"""
	
	homepage = "http://specfun.r-forge.r-project.org/"
	cran = "Bessel" 

	version("0.6-0", md5="0b305edcb9cc81892adbc64f4a8c6897")

	depends_on("r-rmpfr", type=("build", "run"))
