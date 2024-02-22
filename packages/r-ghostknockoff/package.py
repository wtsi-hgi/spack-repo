# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGhostknockoff(RPackage):
	"""The Knockoff Inference Using Summary Statistics

	Functions for multiple knockoff inference using summary statistics, e.g. Z-scores. The knockoff inference is a general procedure for controlling the false discovery rate (FDR) when performing variable selection. This package provides a procedure which performs knockoff inference without ever constructing individual knockoffs (GhostKnockoff). It additionally supports multiple knockoff inference for improved stability and reproducibility. Moreover, it supports meta-analysis of multiple overlapping studies. 
	"""
	
	cran = "GhostKnockoff" 

	version("0.1.0", md5="81263a6f15c0d80126689365a79c00a1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-rdsdp", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-seqminer", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
