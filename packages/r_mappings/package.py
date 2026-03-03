# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMappings(RPackage):
	"""Functions for Transforming Categorical Variables

	Easily create functions to map between different sets of values,
  such as for re-labelling categorical variables.
	"""
	
	homepage = "https://github.com/benjaminrich/mappings"
	cran = "mappings" 

	version("0.1", md5="c3d754c4d3efa1420610dd524764d9fa")

