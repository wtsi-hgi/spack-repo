# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmdvariance(RPackage):
	"""Detecting Differentially Variable Genes Using the Mixture of
Marginal Distributions

	Gene selection based on variance using the marginal distributions of gene profiles that characterized by a mixture of three-component multivariate distributions. Please see the reference: Li X, Fu Y, Wang X, DeMeo DL, Tantisira K, Weiss ST, Qiu W. (2018) <doi:10.1155/2018/6591634>.
	"""
	
	cran = "MMDvariance" 

	version("0.0.9", md5="92c312c0501af9a81a69ae993de20b82")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-lawstat", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
