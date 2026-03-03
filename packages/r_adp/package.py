# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdp(RPackage):
	"""Adoption Probability, Triers and Users Rate of a New Product

	Calculate users prevalence of a product based on the prevalence of triers in the population. The measurement of triers is relatively easy. It is just a question of whether a person tried a product even once in his life or not. On the other hand, The measurement of people who also adopt it as part of their life is more complicated since adopting an innovative product is a subjective view of the individual. Mickey Kislev and Shira Kislev developed a formula to calculate the prevalence of a product's users to overcome this difficulty. The current package assists in calculating the users prevalence of a product based on the prevalence of triers in the population. See for: Kislev, M. M., and S. Kislev (2020) <doi:10.5539/ijms.v12n4p63>.
	"""
	
	cran = "ADP" 

	version("0.1.6", md5="607f46b434ec6a655b860f5401c39654")

