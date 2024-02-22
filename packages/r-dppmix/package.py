# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDppmix(RPackage):
	"""Determinantal Point Process Mixture Models

	Multivariate Gaussian mixture model with a determinant point 
  process prior to promote the discovery of parsimonious components from 
  observed data. See Xu, Mueller, Telesca (2016) <doi:10.1111/biom.12482>.
	"""
	
	homepage = "https://bitbucket.org/djhshih/dppmix"
	cran = "dppmix" 

	version("0.1.1", md5="42c062299e6945b8e594d2c347bde222")

	depends_on("r-mvtnorm", type=("build", "run"))
