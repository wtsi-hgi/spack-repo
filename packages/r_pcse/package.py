# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcse(RPackage):
	"""Panel-Corrected Standard Error Estimation in R

	A function to estimate
        panel-corrected standard errors. Data may contain balanced or
        unbalanced panels.
	"""
	
	cran = "pcse" 

	version("1.9.1.1", md5="33ba410d5b3bb3302a995305a05e658a")

