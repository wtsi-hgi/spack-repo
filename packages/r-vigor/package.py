# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVigor(RPackage):
	"""Variational Bayesian Inference for Genome-Wide Regression

	Conducts linear regression using variational Bayesian inference, particularly optimized for genome-wide association mapping and whole-genome prediction which use a number of DNA markers as the explanatory variables. Provides seven regression models which select the important variables (i.e., the variables related to response variables) among the given explanatory variables in different ways (i.e., model structures).
	"""
	
	cran = "VIGoR" 

	version("1.1.2", md5="9c0da5e00b18879c0dac9afc9f10d7c6")

