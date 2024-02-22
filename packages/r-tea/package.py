# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTea(RPackage):
	"""Threshold Estimation Approaches

	Different approaches for selecting the threshold in generalized Pareto distributions. Most of them are based on minimizing the AMSE-criterion or at least by reducing the bias of the assumed GPD-model. Others are heuristically motivated by searching for stable sample paths, i.e. a nearly constant region of the tail index estimator with respect to k, which is the number of data in the tail. The third class is motivated by graphical inspection. In addition, a sequential testing procedure for GPD-GoF-tests is also implemented here.
	"""
	
	cran = "tea" 

	version("1.1", md5="1db1dc2a41c9ef0ada67bd32b2697812")

	depends_on("r-matrix", type=("build", "run"))
