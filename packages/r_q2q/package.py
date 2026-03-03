# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQ2q(RPackage):
	"""Interpolating Age-Specific Mortality Rates at All Ages

	Mortality Rates are usually published following an abridged description, 
              i.e., by age groups 0, [1, 5[, [5, 10[, [10, 15[ and so on. For some applications, 
              a detailed (single) ages description is required. Despite the huge number of the 
              proposed methods in the literature, there is a limited number of methods ensuring a
              high performance at lower and higher ages in the same time. For example, the 6-terms 
              'Lagrange' interpolation function is well adapted to mortality  interpolation at lower
              ages (with unequal intervals) but is not adapted to higher ages. On the other hand, 
              the 'Karup-King' method allows a good performance at higher ages but not adapted to lower ages.
              Interested readers can refer to the book of Shryock, Siegel and Associates (1993) for a detailed
              overview of the two cited methods.The package Q2q allows combining both the two methods to allow
              interpolating mortality rates at all ages. First, it starts by implementing each method separately,
              then the resulted curves are joined based on a 5-age averaged error between the two curves.
	"""
	
	cran = "Q2q" 

	version("0.1.0", md5="3fee4f73f9be4b71ce8eb2fae6041490")

	depends_on("r@3:", type=("build", "run"))
