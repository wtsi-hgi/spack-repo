# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgal4h(RPackage):
	"""'CGAL' Version 4 C++ Header Files

	'CGAL' is a C++ library that aims to provide easy access to efficient and
  reliable algorithms in computational geometry. Since its version 4, 'CGAL' can be used
  as standalone header-only library and is available under a double GPL-3|LGPL license.
  <https://www.cgal.org/>.
	"""
	
	homepage = "https://gitlab.com/dickoa/cgal4h"
	cran = "cgal4h" 

	version("0.1.0", md5="a7fdb8aa1079f8a061334d85b5a4ffb6")

