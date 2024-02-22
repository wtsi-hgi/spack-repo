# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustetm(RPackage):
	"""Robust Methods using Exponential Tilt Model

	Testing homogeneity for generalized exponential tilt model. This package includes a collection of functions for (1) implementing methods for testing homogeneity for generalized exponential tilt model; and (2) implementing existing methods under comparison.
	"""
	
	cran = "robustETM" 

	version("1.0", md5="18f619082cebea777ad11a58cbd67bf6")

	depends_on("r@2.5:", type=("build", "run"))
