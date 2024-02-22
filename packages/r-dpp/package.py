# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDpp(RPackage):
	"""Inference of Parameters of Normal Distributions from a Mixture
of Normals

	This MCMC method takes a data numeric vector (Y) and assigns the elements of Y
  to a (potentially infinite) number of normal distributions. The individual normal distributions from a mixture of normals can be inferred.
  Following the method described in Escobar (1994) <doi:10.2307/2291223> we use a Dirichlet Process Prior (DPP) to describe stochastically our prior assumptions about the dimensionality of the data.
	"""
	
	cran = "DPP" 

	version("0.1.2", md5="be0673e9204f6fb51cd57617a27f4695")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
