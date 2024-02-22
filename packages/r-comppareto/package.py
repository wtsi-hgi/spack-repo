# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComppareto(RPackage):
	"""Discrete Composite Distributions with Pareto Tails

	Contains the probability density function, cumulative distribution function, quantile function, and random number generator for composite and discrete composite distributions with Pareto tails. The detailed description of the methods and the applications of the methods can be found in Bowen Liu, Malwane M.A. Ananda (2023) <arXiv:2309.16443>. 
	"""
	
	cran = "CompPareto" 

	version("0.1.0", md5="907e22410855792b8ad84d147b015d08")

	depends_on("r-actuar", type=("build", "run"))
