# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarch(RPackage):
	"""Markov Chains

	Computation of various Markovian models for categorical data
    including homogeneous Markov chains of any order, MTD models, Hidden Markov
    models, and Double Chain Markov Models.
	"""
	
	cran = "march" 

	version("3.3.2", md5="c6ee18c350d12a3040d8e0ee8f10a28c")

	depends_on("r@3.5:", type=("build", "run"))
