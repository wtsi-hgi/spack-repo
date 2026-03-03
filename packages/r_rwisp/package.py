# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRwisp(RPackage):
	"""WISP Multiple Criteria Sorting Method

	Implementation of the Integrated Simple Weighted Sum Product Method (WISP), a multiple criteria sorting method create by Dragisa Stanujkic (2021) <doi:10.1109/TEM.2021.3075783>.
	"""
	
	homepage = "https://github.com/dioubernardo/rwisp"
	cran = "rwisp" 

	version("1.0.5", md5="c94a431c5c526c882dabd7d0b6597e99")

