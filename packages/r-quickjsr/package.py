# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuickjsr(RPackage):
	"""Interface for the 'QuickJS' Lightweight 'JavaScript' Engine

	An 'R' interface to the 'QuickJS' portable 'JavaScript' engine.
    The engine is bundled entirely within the package, requiring no external system
    dependencies beyond a 'C' compiler.
	"""
	
	homepage = "https://github.com/andrjohns/QuickJSR"
	cran = "QuickJSR" 

	version("1.1.3", md5="7b343c86102813ebad21d4733928361e")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
