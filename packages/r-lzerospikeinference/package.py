# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLzerospikeinference(RPackage):
	"""Exact Spike Train Inference via L0 Optimization

	An implementation of algorithms described in Jewell and Witten (2017) <arXiv:1703.08644>. 
	"""
	
	cran = "LZeroSpikeInference" 

	version("1.0.3", md5="78bd789fff622d20b8172ed48167f4b7")

