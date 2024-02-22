# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompare(RPackage):
	"""Comparing Objects for Differences

	Functions to compare a model object to a comparison object.
  If the objects are not identical, the functions can be instructed to
  explore various modifications of the objects (e.g., sorting rows,
  dropping names) to see if the modified versions are identical.
	"""
	
	cran = "compare" 

	version("0.2-6", md5="6ba67278ca59db4c5a0aff9e13dcaf2e")

