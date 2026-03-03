# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrequire(RPackage):
	"""Sources an R "Module" with Caching & Encapsulation, Returning
Exported Vars

	In the fashion of 'node.js' <https://nodejs.org/>, requires a file,
  sourcing into the current environment only the variables explicitly specified
  in the module.exports or exports list variable. If the file was already sourced,
  the result of the earlier sourcing is returned to the caller.
	"""
	
	homepage = "https://github.com/rickwargo/lrequire"
	cran = "lrequire" 

	version("0.1.3", md5="515df8dd325a9c72a8c39bb27ed0e334")

	depends_on("r@3.0.1:", type=("build", "run"))
