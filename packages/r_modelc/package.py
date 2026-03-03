# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelc(RPackage):
	"""A Linear Model to 'SQL' Compiler

	This is a cross-platform linear model to 'SQL' compiler. It generates 'SQL' from linear and generalized linear models. Its interface consists of a single function, modelc(), which takes the output of lm() or glm() functions (or any object which has the same signature) and outputs a 'SQL' character vector representing the predictions on the scale of the response variable as described in Dunn & Smith (2018) <doi:10.1007/978-1-4419-0118-7> and originating in Nelder & Wedderburn (1972) <doi:10.2307/2344614>. The resultant 'SQL' can be included in a 'SELECT' statement and returns output similar to that of the glm.predict() or lm.predict() predictions, assuming numeric types are represented in the database using sufficient precision. Currently log and identity link functions are supported.
	"""
	
	homepage = "https://github.com/sparkfish/modelc"
	cran = "modelc" 

	version("1.0.0.0", md5="e07e02f417849f25fb1ac32475bcc390")

