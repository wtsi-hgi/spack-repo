# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROllggamma(RPackage):
	"""Odd Log-Logistic Generalized Gamma Probability Distribution

	Density, distribution function, quantile function and random generation for the Odd Log-Logistic Generalized Gamma proposed in Prataviera, F. et al (2017) <doi:10.1080/00949655.2016.1238088>.
	"""
	
	homepage = "https://mjsaldanha.com/posts/ollggamma"
	cran = "ollggamma" 

	version("1.0.2", md5="4263aaca2638a91c94fbfd70377bc27c")

	depends_on("r@3.1:", type=("build", "run"))
