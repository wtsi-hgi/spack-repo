# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCausalr(RPackage):
	"""Causal network analysis methods

	Causal network analysis methods for regulator prediction and network reconstruction from genome scale data.
	"""
	
	bioc = "CausalR"

	version("1.40.0", commit="7e4e67b884f5d0cbe7f785866b6ad3aa72f8ebbd")
	version("1.34.0", commit="e713478406d99d6bf49e6dedd13c48254e64b45e")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
