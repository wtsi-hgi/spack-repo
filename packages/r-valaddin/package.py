# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RValaddin(RPackage):
	"""Functional Input Validation

	A set of basic tools to transform functions into functions with
    input validation checks, in a manner suitable for both programmatic and
    interactive use.
	"""
	
	homepage = "https://github.com/egnha/valaddin"
	cran = "valaddin" 

	version("1.0.2", md5="8c89d4ca476fbdb488dc027d828b7488")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lazyeval@0.2.1:", type=("build", "run"))
