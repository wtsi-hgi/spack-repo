# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicecondistray(RPackage):
	"""Econometric Production Analysis with Ray-Based Distance
Functions

	Econometric analysis of multiple-input-multiple-output
  production technologies with ray-based input distance functions as suggested
  by Price and Henningsen (2022): "A Ray-Based Input Distance Function to Model
  Zero-Valued Output Quantities: Derivation and an Empirical Application",
  <https://ideas.repec.org/p/foi/wpaper/2022_03.html>.
	"""
	
	homepage = "https://github.com/micEcon/micEconDistRay"
	cran = "micEconDistRay" 

	version("0.1-2", md5="37ba00bc1b99826758f0515a59f42253")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-sfar@0.1.1:", type=("build", "run"))
