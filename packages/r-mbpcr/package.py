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

	version("1.62.0", tag="RELEASE_3_21")
	version("1.56.0", sha256="10834ebe12812383aadca6ebb4e9523debc4d0b917229868ce29cc0d65e7010e")

	depends_on("r-oligoclasses", type=("build", "run"))
	depends_on("r-gwastools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
