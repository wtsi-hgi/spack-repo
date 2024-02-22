# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImediate(RPackage):
	"""Likelihood Methods for Mediation Analysis

	Implements likelihood based methods for mediation analysis. 
	"""
	
	cran = "iMediate" 

	version("0.5.5", md5="ae3ed078ea64d77efeea3223c515c3a7")

	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-mbess", type=("build", "run"))
