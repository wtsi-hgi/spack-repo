# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFancycut(RPackage):
	"""A Fancy Version of 'base::cut'

	Provides the function fancycut() which is like cut() except
  you can mix left open and right open intervals with point values,
  intervals that are closed on both ends and intervals that are open on both ends.
	"""
	
	cran = "fancycut" 

	version("0.1.2", md5="5201659f1c325f173e76bd4190304df1")

