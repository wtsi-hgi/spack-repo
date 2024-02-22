# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinsel(RPackage):
	"""Transform Functions using Decorators

	Instead of nesting function calls, annotate and transform 
    functions using "#." comments.
	"""
	
	homepage = "https://github.com/nteetor/tinsel"
	cran = "tinsel" 

	version("0.0.1", md5="7118f161907b945ddbd54d457c1f5474")

	depends_on("r@3.3.1:", type=("build", "run"))
