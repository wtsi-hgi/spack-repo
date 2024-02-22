# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPalmtree(RPackage):
	"""Partially Additive (Generalized) Linear Model Trees

	This is an implementation of model-based trees with global model
  parameters (PALM trees). The PALM tree algorithm is an extension to the MOB
  algorithm (implemented in the 'partykit' package), where some parameters are
  fixed across all groups. Details about the method can be found in Seibold,
  Hothorn, Zeileis (2016) <arXiv:1612.07498>. The package offers coef(),
  logLik(), plot(), and predict() functions for PALM trees.
	"""
	
	cran = "palmtree" 

	version("0.9-1", md5="354ee731ea571ce49b667e525f4be2f2")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-partykit", type=("build", "run"))
	depends_on("r-formula@1.2.1:", type=("build", "run"))
