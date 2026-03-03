# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspmma(RPackage):
	"""Bayesian Semiparametric Models for Meta-Analysis

	The main functions carry out Gibbs' sampler routines for nonparametric and semiparametric Bayesian models for random effects meta-analysis.
	"""
	
	cran = "bspmma" 

	version("0.1-2", md5="0ae3fe67eb535ffa65530019ce278349")

