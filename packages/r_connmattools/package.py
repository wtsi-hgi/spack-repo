# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConnmattools(RPackage):
	"""Tools for Working with Connectivity Data

	Collects several different methods for analyzing and
    working with connectivity data in R.  Though primarily oriented towards
    marine larval dispersal, many of the methods are general and useful for
    terrestrial systems as well.
	"""
	
	homepage = "https://github.com/dmkaplan2000/ConnMatTools.git"
	cran = "ConnMatTools" 

	version("0.3.5", md5="b747b588c969d1a14ee632332c28cfd1")

