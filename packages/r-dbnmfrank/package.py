# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbnmfrank(RPackage):
	"""Rank Selection for Non-Negative Matrix Factorization

	Given the non-negative data and its distribution, the package estimates the rank parameter for Non-negative Matrix Factorization. The method is based on hypothesis testing, using a deconvolved bootstrap distribution to assess the significance level accurately despite the large amount of optimization error. The distribution of the non-negative data can be either Normal distributed or Poisson distributed.
	"""
	
	cran = "DBNMFrank" 

	version("0.1.0", md5="58908f765d94fb33e75172b50df6760e")

	depends_on("r-nmf", type=("build", "run"))
	depends_on("r-pmledecon@0.2:", type=("build", "run"))
