# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLsvar(RPackage):
	"""Estimation of Low Rank Plus Sparse Structured Vector
Auto-Regressive (VAR) Model

	Implementations of estimation algorithm of low rank plus sparse structured VAR model by using Fast Iterative Shrinkage-Thresholding Algorithm (FISTA). It relates to the algorithm in Sumanta, Li, and Michailidis (2019) <doi:10.1109/TSP.2018.2887401>.
	"""
	
	cran = "LSVAR" 

	version("1.2", md5="2d05e1a9550e6a8e903ad490a9bfd286")

	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
