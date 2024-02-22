# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPspearman(RPackage):
	"""Spearman's Rank Correlation Test

	Spearman's rank correlation test with precomputed exact
        null distribution for n <= 22.
	"""
	
	cran = "pspearman" 

	version("0.3-1", md5="d6a452fcaede228801e565451d986db7")

