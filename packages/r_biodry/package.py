# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodry(RPackage):
	"""Multilevel Modeling of Dendroclimatical Fluctuations

	Multilevel ecological data series (MEDS) are sequences of observations ordered according to temporal/spatial hierarchies that are defined by sample designs, with sample variability confined to ecological factors. Dendroclimatic MEDS of tree rings and climate are modeled into normalized fluctuations of tree growth and aridity.  Modeled fluctuations (model frames) are compared with Mantel correlograms on multiple levels defined by sample design. Package implementation can be understood by running examples in modelFrame(), and muleMan() functions. 
	"""
	
	cran = "BIOdry" 

	version("0.9", md5="aebadd5bcd395e0a6f955bd71d2b4c1c")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-ecodist", type=("build", "run"))
