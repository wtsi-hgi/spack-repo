# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcount(RPackage):
	"""Marginalized Count Regression Models

	Implementation of marginalized models for zero-inflated count data. This package provides a tool to implement an estimation algorithm for the marginalized count models, which
  directly makes inference on the effect of each covariate on the marginal mean of the outcome. 
  The method involves the marginalized zero-inflated Poisson model described 
  in Long et al. (2014) <doi:10.1002/sim.6293>.
	"""
	
	cran = "mcount" 

	version("1.0.0", md5="b42f1b89338114ca54f73ec19dc03466")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-bbmle", type=("build", "run"))
