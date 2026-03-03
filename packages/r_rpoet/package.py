# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpoet(RPackage):
	"""'PoetryDB' API Wrapper

	
  Wrapper for the 'PoetryDB' API <http://poetrydb.org> that allows for interaction and data extraction from the 
  database in an R interface. The 'PoetryDB' API is a database of poetry and poets implemented with 'MongoDB' to 
  enable developers and poets to easily access one of the most comprehensive poetry databases currently available.
	"""
	
	cran = "Rpoet" 

	version("1.1.0", md5="c6ab90158fac48e8de68f4ac9b748003")

