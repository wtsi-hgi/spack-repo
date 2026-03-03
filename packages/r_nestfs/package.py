# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNestfs(RPackage):
	"""Cross-Validated (Nested) Forward Selection

	Implementation of forward selection based on cross-validated
             linear and logistic regression.
	"""
	
	homepage = "https://github.com/mcol/nestfs"
	cran = "nestfs" 

	version("1.0.3", md5="8b5bba755b3e3a90722605b903bdd37e")

	depends_on("r-dgof", type=("build", "run"))
	depends_on("r-proc@1.9:", type=("build", "run"))
