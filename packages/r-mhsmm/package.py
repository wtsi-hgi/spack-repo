# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMhsmm(RPackage):
	"""Inference for Hidden Markov and Semi-Markov Models

	Parameter estimation and prediction for hidden Markov and semi-Markov models for data with multiple observation sequences.  Suitable for equidistant time series data, with multivariate and/or missing data. Allows user defined emission distributions.
	"""
	
	cran = "mhsmm" 

	version("0.4.21", md5="f31ad965a28d4a6fe83ecd659ee53cad")

	depends_on("r-mvtnorm", type=("build", "run"))
