# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeplogo(RPackage):
	"""Dependency Logo

	Plots dependency logos from a set of aligned input sequences.
	"""
	
	cran = "DepLogo" 

	version("1.2.1", md5="bacf451e83094c61ca4183f1d922c19e")

