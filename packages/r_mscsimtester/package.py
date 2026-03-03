# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMscsimtester(RPackage):
	"""Tests of Multispecies Coalescent Gene Tree Simulator Output

	Statistical tests for validating multispecies coalescent gene tree simulators, using pairwise distances and rooted triple counts. Background is given by Allman, Banos, and Rhodes (2019) <arXiv:1908.01424>. 
	"""
	
	cran = "MSCsimtester" 

	version("1.0.0", md5="d1e808d0dd156896c3a000b48e120a33")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
