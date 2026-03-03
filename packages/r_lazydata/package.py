# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLazydata(RPackage):
	"""A LazyData Facility

	Supplies a LazyData facility for packages which have data
		sets but do not provide LazyData: true.  A single function is
		is included, requireData, which is a drop-in replacement for
		base::require, but carrying the additional
		functionality. By default, it suppresses package
		startup messages as well.  See argument 'reallyQuitely'.
	"""
	
	cran = "lazyData" 

	version("1.1.0", md5="b7d34e45b43c83b94d07242a8b7353aa")

	depends_on("r@2.15:", type=("build", "run"))
