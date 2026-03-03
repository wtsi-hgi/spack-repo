# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtdaNi(RPackage):
	"""Doubly Truncated Data Analysis, Non Iterative

	Non-iterative estimator for the cumulative distribution of a doubly truncated variable. de Uña-Álvarez J. (2018) <doi:10.1007/978-3-319-73848-2_37>.
	"""
	
	homepage = "https://github.com/sidoruvigo/DTDA.ni"
	cran = "DTDA.ni" 

	version("1.0.1", md5="e0f4f5abf57208aa5a1db70471d8c520")

	depends_on("r@3.3:", type=("build", "run"))
