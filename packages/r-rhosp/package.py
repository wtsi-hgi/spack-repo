# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRhosp(RPackage):
	"""Side Effect Risks in Hospital : Simulation and Estimation

	Evaluating risk (that a patient arises a side effect) during hospitalization is the main purpose of this package. Several methods (Parametric, non parametric and De Vielder estimation) to estimate the risk constant (R) are implemented in this package. There are also functions to simulate the different models of this issue in order to quantify the previous estimators. It is necessary to read at least the first six pages of the report to understand the topic.
	"""
	
	cran = "rhosp" 

	version("1.10", md5="7211fc167a17faf5256b808a301d3d1c")

