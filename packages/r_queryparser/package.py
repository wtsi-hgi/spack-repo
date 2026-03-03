# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQueryparser(RPackage):
	"""Translate 'SQL' Queries into 'R' Expressions

	Translate 'SQL' 'SELECT' statements into lists of 'R' expressions.
	"""
	
	homepage = "https://github.com/ianmcook/queryparser"
	cran = "queryparser" 

	version("0.3.2", md5="b7c4292f48b1ad48dc2d8aa8b8ce0867")

