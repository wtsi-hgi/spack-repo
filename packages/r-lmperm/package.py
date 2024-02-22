# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLmperm(RPackage):
	"""Permutation Tests for Linear Models

	Linear model functions using permutation tests.
	"""
	
	homepage = "https://github.com/mtorchiano/lmPerm"
	cran = "lmPerm" 

	version("2.1.0", md5="d070067999795de6f98cbb307e4118c1")

