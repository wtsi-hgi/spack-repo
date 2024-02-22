# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHeterogen(RPackage):
	"""Spatial Functions for Heterogeneity and Climate Variability

	A comprehensive suite of spatial 
  functions created to analyze and assess data heterogeneity and climate variability 
  in spatial datasets. This package is specifically designed to address the challenges associated
  with characterizing and understanding complex spatial patterns in environmental and climate-related data.
	"""
	
	homepage = "https://github.com/patauchi/heterogen"
	cran = "heterogen" 

	version("1.2.33", md5="30f25a1913d3b61208332b035ad0575b")

	depends_on("r-terra", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
