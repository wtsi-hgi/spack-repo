# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmsurv(RPackage):
	"""Data sets from Klein and Moeschberger (1997), Survival Analysis

	Data sets and functions for Klein and Moeschberger (1997),
        "Survival Analysis, Techniques for Censored and Truncated
        Data", Springer.
	"""
	
	cran = "KMsurv" 

	version("0.1-5", md5="4979464e3ee73b03891b66e53231b2be")

