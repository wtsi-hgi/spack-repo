# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPowergwasinteraction(RPackage):
	"""Power Calculations for GxE and GxG Interactions for GWAS

	Analytical power calculations for GxE and GxG interactions for case-control studies of candidate genes and genome-wide association studies (GWAS). This includes power calculation for four two-step screening and testing procedures.  It can also calculate power for GxE and GxG without any screening.    
	"""
	
	cran = "powerGWASinteraction" 

	version("1.1.3", md5="91608c03653896577d0183bc8eec90c7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-pwr", type=("build", "run"))
