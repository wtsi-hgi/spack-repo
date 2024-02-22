# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMuhaz(RPackage):
	"""Hazard Function Estimation in Survival Analysis

	Produces a smooth estimate of the hazard
  function for censored data.
	"""
	
	cran = "muhaz" 

	version("1.2.6.4", md5="6021d80354ee966f0d7be4ba6ce8c2d1")

	depends_on("r@2.3:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
