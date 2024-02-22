# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFuzzyresampling(RPackage):
	"""Resampling Methods for Triangular and Trapezoidal Fuzzy Numbers

	The classical (i.e. Efron's, see Efron and Tibshirani (1994, ISBN:978-0412042317)  "An Introduction to the Bootstrap") bootstrap is widely used for both the real (i.e. "crisp") and fuzzy data.
 The main aim of the algorithms implemented in this package  is to overcome a problem with repetition of a few distinct values and to create fuzzy numbers, which are "similar" (but not the same) to values from the initial sample.
 To do this, different characteristics of triangular/trapezoidal numbers are kept (like the value, the ambiguity, etc., see Grzegorzewski et al. <doi:10.2991/eusflat-19.2019.68>, Grzegorzewski et al. (2020) <doi:10.2991/ijcis.d.201012.003>, Grzegorzewski et al. (2020) <doi:10.34768/amcs-2020-0022>, Grzegorzewski and Romaniuk (2022) <doi:10.1007/978-3-030-95929-6_3>,  Romaniuk and Hryniewicz (2019) <doi:10.1007/s00500-018-3251-5>).
 Some additional procedures related to these resampling methods are also provided,
 like calculation of the Bertoluzza et al.'s distance (aka the mid/spread distance, see Bertoluzza et al. (1995) "On a new class of distances between fuzzy numbers")
 and estimation of the p-value of the one- and two- sample bootstrapped test for the mean (see Lubiano et al. (2016, <doi:10.1016/j.ejor.2015.11.016>)).
 Additionally, there are procedures which randomly generate trapezoidal fuzzy numbers using some well-known statistical distributions.
	"""
	
	homepage = "https://github.com/mroman-ibs/FuzzyResampling"
	cran = "FuzzyResampling" 

	version("0.6.3", md5="82ed8f707e14a7b7c414c3720b13f7ef")

