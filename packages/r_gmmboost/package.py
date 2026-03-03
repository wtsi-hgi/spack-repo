# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmmboost(RPackage):
	"""Likelihood-Based Boosting for Generalized Mixed Models

	Likelihood-based boosting approaches for generalized mixed models are provided.
	"""
	
	cran = "GMMBoost" 

	version("1.1.5", md5="66551c1bcba62465fe769709816321ad")

	depends_on("r-minqa", type=("build", "run"))
	depends_on("r-magic", type=("build", "run"))
