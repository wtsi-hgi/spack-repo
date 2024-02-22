# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDiscretization(RPackage):
	"""Data Preprocessing, Discretization for Classification

	A collection of supervised discretization
        algorithms. It can also be grouped in terms of top-down or
        bottom-up, implementing the discretization algorithms.
	"""
	
	cran = "discretization" 

	version("1.0-1.1", md5="dbdc36b0db148ea09bed2a4c91a99c39")

