# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamHp(RPackage):
	"""Hierarchical Partitioning of Adjusted R2 and Explained Deviance
for Generalized Additive Models

	Conducts hierarchical partitioning to calculate individual contributions of each predictor towards adjusted R2 and explained deviance for generalized additive models based on output of gam()in 'mgcv' package, applying the algorithm in this paper: Lai(2022) <doi:10.1093/jpe/rtac096>.
	"""
	
	homepage = "https://github.com/laijiangshan/gam.hp"
	cran = "gam.hp" 

	version("0.0-1", md5="201915ffb468c7dfa84917288a84a7fc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
