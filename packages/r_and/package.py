# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnd(RPackage):
	"""Construct Natural-Language Lists with Internationalization

	Construct language-aware lists. Make "and"-separated and
    "or"-separated lists that automatically conform to the user's language
    settings.
	"""
	
	homepage = "https://pkg.rossellhayes.com/and/"
	cran = "and" 

	version("0.1.5", md5="c2e64bba166e9a103e438f7f45373b8f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
