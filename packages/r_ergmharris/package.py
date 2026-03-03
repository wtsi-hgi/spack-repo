# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErgmharris(RPackage):
	"""Local Health Department network data set

	Data for use with the Sage Introduction to Exponential
        Random Graph Modeling text by Jenine K. Harris.  Network data
        set consists of 1283 local health departments and the
        communication links among them along with several attributes.
	"""
	
	cran = "ergmharris" 

	version("1.0", md5="e0de6e68d959035ae60d2ccdf946f2b2")

