# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPiper(RPackage):
	"""Multi-Paradigm Pipeline Implementation

	Provides various styles of function chaining methods: Pipe
    operator, Pipe object, and pipeline function, each representing a distinct
    pipeline model yet sharing almost a common set of features: A value can be
    piped to the first unnamed argument of a function and to dot symbol in an
    enclosed expression. The syntax is designed to make the pipeline more
    readable and friendly to a wide range of operations.
	"""
	
	homepage = "https://renkun.me/pipeR"
	cran = "pipeR" 

	version("0.6.1.3", md5="00531f33dc07ae2a4a362b6b6cf4222f")

	depends_on("r@2.15:", type=("build", "run"))
