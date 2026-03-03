# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBspec(RPackage):
	"""Bayesian Spectral Inference

	Bayesian inference on the (discrete) power spectrum of time series.
	"""
	
	cran = "bspec" 

	version("1.6", md5="6d2e7c1209d21898eaf03f2d0ca973c4")

