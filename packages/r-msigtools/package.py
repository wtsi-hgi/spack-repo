# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsigtools(RPackage):
	"""Mutational Signature Analysis Tools

	Utility functions for mutational signature analysis
             as described in Alexandrov, L. B. (2020)
             <doi:10.1038/s41586-020-1943-3>.
             This package provides two groups of functions. One is
             for dealing with mutational signature "exposures"
             (i.e. the counts of mutations in a sample that are
             due to each mutational signature). The other group of
             functions is for matching or comparing sets of 
             mutational signatures. 'mSigTools' stands for 
             mutational Signature analysis Tools. 
	"""
	
	homepage = "https://github.com/Rozen-Lab/mSigTools"
	cran = "mSigTools" 

	version("1.0.7", md5="2a72c64b1c6b511493de06f9fc6aeba4")

	depends_on("r-clue", type=("build", "run"))
	depends_on("r-philentropy", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-sets", type=("build", "run"))
