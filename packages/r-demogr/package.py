# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemogr(RPackage):
	"""Analysis of Age-Structured Demographic Models

	Construction and analysis of matrix population models in R.
	"""
	
	cran = "demogR" 

	version("0.6.0", md5="7b21de430418f7ab6da8d05fa50b28bc")

