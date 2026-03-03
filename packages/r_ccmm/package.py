# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcmm(RPackage):
	"""Compositional Mediation Model

	Estimate the direct and indirect (mediation) effects of treatment on the outcome when intermediate variables (mediators) are compositional and high-dimensional. Sohn, M.B. and Li, H. (2017). Compositional Mediation Analysis for Microbiome Studies. (AOAS: In revision).
	"""
	
	cran = "ccmm" 

	version("1.0", md5="85fd351ed432685ee324e465225b5ca2")

	depends_on("r-mass", type=("build", "run"))
