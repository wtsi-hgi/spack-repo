# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLenses(RPackage):
	"""Elegant Data Manipulation with Lenses

	Provides tools for creating and using lenses to simplify data manipulation. Lenses are composable getter/setter pairs for working with data in a purely functional way. Inspired by the 'Haskell' library 'lens' (Kmett, 2012) <https://hackage.haskell.org/package/lens>. For a fairly comprehensive (and highly technical) history of lenses please see the 'lens' wiki <https://github.com/ekmett/lens/wiki/History-of-Lenses>.
	"""
	
	homepage = "http://cfhammill.github.io/lenses"
	cran = "lenses" 

	version("0.0.3", md5="a7ce0b74cadb5958a07fea7e75046200")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
