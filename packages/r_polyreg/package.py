# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPolyreg(RPackage):
	"""Polynomial Regression

	Automate formation and evaluation of polynomial regression models. The motivation for this package is described in 'Polynomial Regression As an Alternative to Neural Nets' by Xi Cheng, Bohdan Khomtchouk, Norman Matloff, and Pete Mohanty (<arXiv:1806.06850>).
	"""
	
	homepage = "https://github.com/matloff/polyreg"
	cran = "polyreg" 

	version("0.8.0", md5="b5e7cc05275940c1f04a649eb8ba794c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
