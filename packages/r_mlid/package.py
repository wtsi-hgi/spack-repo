# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlid(RPackage):
	"""Multilevel Index of Dissimilarity

	Tools and functions to fit a multilevel index of dissimilarity.
	"""
	
	homepage = "https://github.com/profrichharris/MLID"
	cran = "MLID" 

	version("1.0.1", md5="44dfa8f0c82fad641536a68588adbf4c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-nlme@3.1.128:", type=("build", "run"))
	depends_on("r-lme4@1.1.12:", type=("build", "run"))
