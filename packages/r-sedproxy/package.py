# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSedproxy(RPackage):
	"""Simulation of Sediment Archived Climate Proxy Records

	Proxy forward modelling for sediment archived climate proxies such 
  as Mg/Ca, d18O or Alkenones. The user provides a hypothesised "true" past climate, 
  such as output from a climate model, and details of the sedimentation rate and 
  sampling scheme of a sediment core. Sedproxy returns simulated proxy records. 
  Implements the methods described in Dolman and Laepple (2018) 
  <doi:10.5194/cp-14-1851-2018>.
	"""
	
	homepage = "https://earthsystemdiagnostics.github.io/sedproxy/"
	cran = "sedproxy" 

	version("0.7.5", md5="3fcd7b2e38f5e1efada2668b46e70848")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
