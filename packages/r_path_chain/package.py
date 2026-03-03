# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathChain(RPackage):
	"""Concise Structure for Chainable Paths

	Provides path_chain class and functions, which facilitates loading and saving 
             directory structure in YAML configuration files via 'config' package. 
             The file structure you created during exploration can be transformed 
             into legible section in the config file, and then easily loaded for further usage.
	"""
	
	homepage = "https://github.com/krzjoa/path.chain"
	cran = "path.chain" 

	version("0.2.0", md5="44569879943d6175487ecb7e2fa960e0")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-logger", type=("build", "run"))
