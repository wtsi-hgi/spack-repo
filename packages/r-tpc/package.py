# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTpc(RPackage):
	"""Tiered PC Algorithm

	Constraint-based causal discovery using the PC algorithm while
    accounting for a partial node ordering, for example a partial temporal ordering
    when the data were collected in different waves of a cohort study.
    Andrews RM, Foraita R, Didelez V, Witte J (2021) <arXiv:2108.13395>  
    provide a guide how to use tpc to analyse cohort data.
	"""
	
	homepage = "https://github.com/bips-hb/tpc"
	cran = "tpc" 

	version("1.0", md5="65b815b875bb99a069e0c616e386df7e")

	depends_on("r-pcalg", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
