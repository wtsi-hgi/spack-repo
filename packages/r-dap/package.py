# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDap(RPackage):
	"""Discriminant Analysis via Projections

	An implementation of Discriminant Analysis via Projections (DAP) method for high-dimensional binary classification in the case of unequal covariance matrices. See Irina Gaynanova and Tianying Wang (2018) <arXiv:1711.04817v2>.
	"""
	
	homepage = "http://github.com/irinagain/DAP"
	cran = "DAP" 

	version("1.0", md5="c72d1652598d7a6b2bc01d7dcf0d7ca7")

	depends_on("r-mass", type=("build", "run"))
