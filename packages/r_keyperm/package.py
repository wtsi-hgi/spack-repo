# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeyperm(RPackage):
	"""Keyword Analysis Using Permutation Tests

	Efficient implementation of permutation tests for keyword analysis in corpus linguistics as described in Mildenberger (2023) <arXiv:2308.13383>.
	"""
	
	cran = "keyperm" 

	version("0.1.1", md5="97d06799649afc3f4f1d9d631e39c874")

	depends_on("r-slam", type=("build", "run"))
	depends_on("r-tm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
