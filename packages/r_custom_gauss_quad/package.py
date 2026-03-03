# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCustomGaussQuad(RPackage):
	"""Custom Made Gauss Quadrature Nodes and Weights

	
    Use the high-precision arithmetic provided by the R package 'Rmpfr' 
    to compute a custom-made Gauss quadrature nodes and weights, 
    with up to 33 nodes, using a moment-based method via moment 
    determinants. Paul Kabaila (2022) <arXiv:2211.04729>.
	"""
	
	cran = "custom.gauss.quad" 

	version("1.0.0", md5="ddfb5a4b198c658424c5583625a115ed")

	depends_on("r-rmpfr", type=("build", "run"))
