# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMvnpermute(RPackage):
	"""Generate New Multivariate Normal Samples from Permutations

	Given a vector of multivariate normal data, a matrix of
    covariates and the data covariance matrix, generate new multivariate normal
    samples that have the same covariance matrix based on permutations of
    the transformed data residuals.
	"""
	
	homepage = "https://github.com/markabney/MVNpermute"
	cran = "mvnpermute" 

	version("1.0.1", md5="ba57fd16c842484592dd34893e388026")

