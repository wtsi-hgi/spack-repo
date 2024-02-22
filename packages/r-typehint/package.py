# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTypehint(RPackage):
	"""Auto-Check Types, Dimensions, and Values of Function Arguments

	Type hints are special comments within a function body indicating the intended nature of the function's arguments in terms of data types, dimensions and permitted values. The actual parameters with which the function is called are evaluated against these type hint comments at run-time.
	"""
	
	homepage = "https://github.com/jsugarelli/typehint/"
	cran = "typehint" 

	version("0.1.2", md5="baab143551060e52e05f1ba1d867af9b")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
