# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAppnn(RPackage):
	"""Amyloid Propensity Prediction Neural Network

	Amyloid propensity prediction neural network (APPNN) is an amyloidogenicity propensity predictor based on a machine learning approach through recursive feature selection and feed-forward neural networks, taking advantage of newly published sequences with experimental, in vitro, evidence of amyloid formation.
	"""
	
	cran = "appnn" 

	version("1.0-0", md5="f9c48ab688fe59d0e7df9d358710d0a6")

