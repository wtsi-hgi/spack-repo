# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBraidrm(RPackage):
	"""Fitting Dose Response with the BRAID Combined Action Model

	Contains functions for evaluating, analyzing, and fitting combined action dose response surfaces with the Bivariate Response to Additive Interacting Dose (BRAID) model of combined action.
	"""
	
	cran = "braidrm" 

	version("0.71", md5="d6e15f0dedfe4c786e4cbef97f444529")

