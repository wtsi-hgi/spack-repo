# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNseval(RPackage):
	"""Tools for Lazy and Non-Standard Evaluation

	Functions to capture, inspect, manipulate, and create
             lazy values (promises), "..." lists, and active calls.
	"""
	
	cran = "nseval" 

	version("0.5.1", md5="a5dc81f99bef034d89e14bc80c2bac8b")

