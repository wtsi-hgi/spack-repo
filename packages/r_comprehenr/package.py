# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComprehenr(RPackage):
	"""List Comprehensions

	Provides 'Python'-style list comprehensions.
    List comprehension expressions use usual loops (for(), while() and repeat()) and
    usual if() as list producers. In many cases it gives more concise notation than
    standard "*apply + filter" strategy.
	"""
	
	homepage = "https://github.com/gdemin/comprehenr"
	cran = "comprehenr" 

	version("0.6.10", md5="02f3c79d161b77c46295adda537a9ade")

	depends_on("r@3.3:", type=("build", "run"))
