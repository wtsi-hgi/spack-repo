# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCobs(RPackage):
	"""Constrained B-Splines (Sparse Matrix Based)

	Qualitatively Constrained (Regression) Smoothing Splines via
        Linear Programming and Sparse Matrices.
	"""
	
	homepage = "https://curves-etc.r-forge.r-project.org/"
	cran = "cobs" 

	version("1.3-8", md5="8b771c4ee912ba9eb3d22182bfcc3c6f")

	depends_on("r-sparsem@1.6:", type=("build", "run"))
	depends_on("r-quantreg@4.65:", type=("build", "run"))
