# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPenaltylearning(RPackage):
	"""Penalty Learning

	Implementations of algorithms from 
 Learning Sparse Penalties for Change-point Detection
 using Max Margin Interval Regression, by
 Hocking, Rigaill, Vert, Bach
 <http://proceedings.mlr.press/v28/hocking13.html>
 published in proceedings of ICML2013.
	"""
	
	homepage = "https://github.com/tdhock/penaltyLearning"
	cran = "penaltyLearning" 

	version("2024.1.25", md5="585b957f90c1c8c435f9c5cf0ed7bc5a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table@1.9.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
