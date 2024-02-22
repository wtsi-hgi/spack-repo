# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrp(RPackage):
	"""Bayesian Prior and Posterior Predictive Replication Assessment

	Utilize the Bayesian prior and posterior predictive checking
   approach to provide a statistical assessment of replication success 
   and failure. The package is based on the methods proposed in 
   Zhao,Y., Wen X.(2021) <arXiv:2105.03993>. 
	"""
	
	cran = "PRP" 

	version("0.1.1", md5="864761a1428ca1dc15a9fa2dc2213119")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
