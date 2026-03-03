# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTsdf(RPackage):
	"""Two-/Three-Stage Designs for Phase 1&2 Clinical Trials

	Calculate optimal Zhong's two-/three-stage Phase II designs (see Zhong (2012) <doi:10.1016/j.cct.2012.07.006>). Generate Target Toxicity decision table for Phase I dose-finding (two-/three-stage). This package also allows users to run dose-finding simulations based on customized decision table. 
	"""
	
	cran = "tsdf" 

	version("1.1-8", md5="a493ffaa64db0a4edbbd3866a16444c0")

