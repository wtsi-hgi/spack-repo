# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbpcr(RPackage):
	"""Bayesian Piecewise Constant Regression for DNA copy number estimation

	It contains functions for estimating the DNA copy number profile using mBPCR with the aim of detecting regions with copy number changes.
	"""
	
	homepage = "http://www.idsia.ch/~paola/mBPCR"
	bioc = "mBPCR"

	version("1.62.0", commit="4a6953f248a93d0bfd313f61b579651afcb68bf5")
	version("1.56.0", commit="e983807897a64230cc0407f0739ab24af74f328e")

	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-gwastools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
