# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsm(RPackage):
	"""Fit and Analyze Smooth Supersaturated Models

	Creates an S4 class "SSM" and defines functions for fitting smooth
    supersaturated models, a polynomial model with spline-like behaviour.
    Functions are defined for the computation of Sobol indices for sensitivity
    analysis and plotting the main effects using FANOVA methods. It also
    implements the estimation of the SSM metamodel error using a GP model with
    a variety of defined correlation functions.
	"""
	
	homepage = "https://github.com/peterrobertcurtis/SSM"
	cran = "SSM" 

	version("1.0.1", md5="6c0a68470fbfe57ec6494302fe176aa5")

