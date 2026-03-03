# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFspe(RPackage):
	"""Estimating the Number of Factors in EFA with Out-of-Sample
Prediction Errors

	Estimating the number of factors in Exploratory Factor Analysis (EFA) with out-of-sample prediction errors using a cross-validation scheme. Haslbeck & van Bork (Preprint) <https://psyarxiv.com/qktsd>.
	"""
	
	cran = "fspe" 

	version("0.1.2", md5="93e135b3e57bf89d4b54e00ba5efccfc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
