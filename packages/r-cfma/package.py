# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfma(RPackage):
	"""Causal Functional Mediation Analysis

	Performs causal functional mediation analysis (CFMA) for functional treatment, functional mediator, and functional outcome. This package includes two functional mediation model types: (1) a concurrent mediation model and (2) a historical influence mediation model. See Zhao et al. (2018), Functional Mediation Analysis with an Application to Functional Magnetic Resonance Imaging Data, <arXiv:1805.06923> for details.
	"""
	
	cran = "cfma" 

	version("1.0", md5="54f490d519fef20330e2501b7fe7002c")

	depends_on("r@2.10:", type=("build", "run"))
