# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenenet(RPackage):
	"""Modeling and Inferring Gene Networks

	Analyzes gene expression
  (time series) data with focus on the inference of gene networks.
  In particular, GeneNet implements the methods of Schaefer and 
  Strimmer (2005a,b,c) and Opgen-Rhein and Strimmer (2006, 2007)
  for learning large-scale gene association networks (including
  assignment of putative directions).  
	"""
	
	homepage = "https://strimmerlab.github.io/software/genenet/"
	cran = "GeneNet" 

	version("1.2.16", md5="8547162999d1f2af1cf03389f2b27a57")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-corpcor@1.6.10:", type=("build", "run"))
	depends_on("r-longitudinal@1.1.13:", type=("build", "run"))
	depends_on("r-fdrtool@1.2.17:", type=("build", "run"))
