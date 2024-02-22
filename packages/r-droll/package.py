# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDroll(RPackage):
	"""Analyze Roll Distributions

	A toolkit for parsing dice notation, analyzing rolls,
    calculating success probabilities, and plotting outcome distributions.
	"""
	
	cran = "droll" 

	version("0.1.0", md5="004e799726bf809733788e93364db56f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ryacas", type=("build", "run"))
