# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNutrition(RPackage):
	"""Useful Functions for People on a Diet

	Contains a collection of functions for performing different kinds
    of calculation that are of interest to someone following a diet plan.
    Calculators for the Basal Metabolic Rate are based on Mifflin et al. (1990)
    <doi:10.1093/ajcn/51.2.241> and  McArdle, W. D., Katch, F. I., &
    Katch, V. L. (2010, ISBN:9780812109917).
	"""
	
	homepage = "https://wleoncio.github.io/nutrition/"
	cran = "nutrition" 

	version("1.1.0", md5="32dafa92cdb00bc30f63bb0fa4d0bacf")

