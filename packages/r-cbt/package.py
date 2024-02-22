# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbt(RPackage):
	"""Confidence Bound Target Algorithm

	The Confidence Bound Target (CBT) algorithm is designed for infinite arms bandit problem. It is shown that CBT algorithm achieves the regret lower bound for general reward distributions. Reference: Hock Peng Chan and Shouri Hu (2018) <arXiv:1805.11793>.
	"""
	
	cran = "CBT" 

	version("1.0", md5="86974758fc06b5da6f02e0d4e7941179")

