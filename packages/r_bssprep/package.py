# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBssprep(RPackage):
	"""Whitening Data as Preparation for Blind Source Separation

	Whitening is the first step of almost all blind source separation (BSS) methods. A fast implementation of whitening for BSS is implemented to serve as a lightweight dependency for packages providing BSS methods.
	"""
	
	cran = "BSSprep" 

	version("0.1", md5="fe218cb66459d277d62cb3b1031960ab")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
