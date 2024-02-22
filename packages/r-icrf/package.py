# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcrf(RPackage):
	"""Interval Censored Recursive Forests

	Implements interval censored recursive forests (ICRF) based on Cho, Jewell, and Kosorok (2021+). 
            ICRF is a variant of random forests where the outcome variable is interval censored survival data.
            It can be used for usual right censored data and current status data as well.
            A recursion technique is used to improve accuracy and smoothed survival curves are provided.
	"""
	
	cran = "icrf" 

	version("2.0.2", md5="c91a6660ae9e331f927b1008c35c7677")

	depends_on("r@3.5:", type=("build", "run"))
