# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtype(RPackage):
	"""A strong type system for R

	A strong type system for R which supports
    symbol declaration and assignment with type checking
    and condition checking.
	"""
	
	homepage = "http://renkun.me/rtype"
	cran = "rtype" 

	version("0.1-1", md5="490c2e5386c2f29cfbb2a998ee938037")

	depends_on("r@2.15:", type=("build", "run"))
