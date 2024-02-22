# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenderinfer(RPackage):
	"""This is a Collection of Functions to Analyse Gender Differences

	Implementation of functions, which combines binomial calculation 
    and data visualisation, to analyse the differences in publishing authorship
    by gender described in Day et al. (2020) <doi:10.1039/C9SC04090K>.
    It should only be used when self-reported gender is unavailable.
	"""
	
	cran = "GenderInfer" 

	version("0.1.0", md5="f72cf50015b2e59b01d16cf73e9127c3")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
