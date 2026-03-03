# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKnockoffhybrid(RPackage):
	"""Hybrid Analysis of Population and Trio Data with Knockoff
Statistics for FDR Control

	Identification of putative causal variants in genome-wide association studies using hybrid analysis of both the trio and population designs. 
	"""
	
	cran = "KnockoffHybrid" 

	version("1.0.0", md5="4957d3a7da1971bd99e1d8be9402c69b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-spatest", type=("build", "run"))
