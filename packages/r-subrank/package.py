# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubrank(RPackage):
	"""Computes Copula using Ranks and Subsampling

	Estimation of copula using ranks and subsampling. The main feature of this method is that simulation studies show a low sensitivity to dimension, on realistic cases.
	"""
	
	cran = "subrank" 

	version("0.9.9.3", md5="463637d35119ef67a1a3592009a26eae")

