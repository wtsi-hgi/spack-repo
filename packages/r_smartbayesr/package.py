# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmartbayesr(RPackage):
	"""Bayesian Set of Best Dynamic Treatment Regimes and Sample Size
in SMARTs for Binary Outcomes

	Permits determination of a set of 
    optimal dynamic treatment regimes and sample size for a SMART design 
    in the Bayesian setting with binary outcomes. Please see Artman (2020) <arXiv:2008.02341>.
	"""
	
	cran = "SMARTbayesR" 

	version("2.0.0", md5="3a8ce9351e08995087c5e1c2b9c35cc5")

	depends_on("r-laplacesdemon", type=("build", "run"))
