# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKerdaa(RPackage):
	"""New Kernel-Based Test for Differential Association Analysis

	A new practical method to evaluate whether relationships between two sets of high-dimensional variables are different or not across two conditions.
    Song, H. and Wu, M.C. (2023) 
    <arXiv:2307.15268>.
	"""
	
	cran = "kerDAA" 

	version("0.1.1", md5="7a396c14f7cd421c6eb25032780051b7")

	depends_on("r-mvtnorm", type=("build", "run"))
