# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpcompute(RPackage):
	"""Compute Power or Sample Size for GWAS with Covariate Effect

	Fast computation of the required sample size or the
    achieved power, for GWAS studies with different types of covariate
    effects and different types of covariate-gene dependency structure.
    For the detailed description of the methodology, see Zhang (2022)
    "Power and Sample Size Computation for Genetic Association Studies
     of Binary Traits: Accounting for Covariate Effects" <arXiv:2203.15641>.
	"""
	
	cran = "SPCompute" 

	version("1.0.3", md5="274f38d1a2d470ceac95fdee8e5bb29c")

	depends_on("r-matrix", type=("build", "run"))
