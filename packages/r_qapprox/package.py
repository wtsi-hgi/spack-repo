# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQapprox(RPackage):
	"""Approximation to the Survival Functions of Quadratic Forms of
Gaussian Variables

	Calculates the right-tail probability of quadratic forms of Gaussian variables using the skewness-kurtosis ratio matching method, modified Liu-Tang-Zhang method and Satterthwaite-Welch method. The technical details can be found in Hong Zhang, Judong Shen and Zheyang Wu (2020) <arXiv:2005.00905>.
	"""
	
	cran = "Qapprox" 

	version("0.2.0", md5="670e9fc9da9a8a47128174d491b2ec84")

