# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnames(RPackage):
	"""Recursive Display of Items in Nested Lists

	Recursive display of names and paths of all the items nested within sublists of a list object.
	"""
	
	cran = "rnames" 

	version("1.0.1", md5="7cb09b1964601aa834f181ba45d299ef")

