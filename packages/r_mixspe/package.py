# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixspe(RPackage):
	"""Mixtures of Power Exponential and Skew Power Exponential
Distributions for Use in Model-Based Clustering and
Classification

	Mixtures of skewed and elliptical distributions are implemented using mixtures of multivariate skew 
    power exponential and power exponential distributions, respectively. A generalized expectation-maximization 
    framework is used for parameter estimation. See citation() for how to cite.
	"""
	
	cran = "mixSPE" 

	version("0.9.2", md5="b1120eef278e9fedc5fed69845bc4b48")

	depends_on("r-mvtnorm", type=("build", "run"))
