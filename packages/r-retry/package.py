# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRetry(RPackage):
	"""Repeated Evaluation

	Provide simple mechanism to repeatedly evaluate an expression until either it succeeds or timeout exceeded. It is useful in situations that random failures could happen.
	"""
	
	homepage = "https://github.com/randy3k/retry"
	cran = "retry" 

	version("0.1.1", md5="05821a012b855541fa1b6ce73c319ca0")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-later", type=("build", "run"))
