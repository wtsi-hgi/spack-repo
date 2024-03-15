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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/mBPCR_1.56.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/mBPCR/mBPCR_1.56.0.tar.gz"]

	version("1.56.0", md5="1d48a3fd5a04c61ce96aa4da34d364a2")

	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-gwastools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
