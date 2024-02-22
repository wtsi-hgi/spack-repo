# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMar(RPackage):
	"""Multivariate AutoRegressive Analysis

	R functions for the estimation and eigen-decomposition of multivariate autoregressive models.
	"""
	
	cran = "mAr" 

	version("1.2-0", md5="d0dff48ad8b5d5642ce3b229d5e1524f")

	depends_on("r-mass", type=("build", "run"))
