# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFpopw(RPackage):
	"""Weighted Segmentation using Functional Pruning and Optimal
Partioning

	Weighted-L2 FPOP Maidstone et al. (2017) <doi:10.1007/s11222-016-9636-3> and pDPA/FPSN Rigaill (2010) <arXiv:1004.0887> algorithm for detecting multiple changepoints in the mean of a vector. Also includes a few model selection functions using Lebarbier (2005) <doi:10.1016/j.sigpro.2004.11.012> and the 'capsushe' package.
	"""
	
	cran = "fpopw" 

	version("1.1", md5="79c6424ac390b23039e8173ee0014c3a")

	depends_on("r@3.1:", type=("build", "run"))
