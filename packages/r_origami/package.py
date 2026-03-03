# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrigami(RPackage):
	"""Generalized Framework for Cross-Validation

	A general framework for the application of cross-validation schemes
    to particular functions. By allowing arbitrary lists of results, origami
    accommodates a range of cross-validation applications. This implementation
    was first described by Coyle and Hejazi (2018) <doi:10.21105/joss.00512>.
	"""
	
	homepage = "https://tlverse.org/origami/"
	cran = "origami" 

	version("1.0.7", md5="7b73e2299fcb86cb1ebb1b33ff95d5b1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-listenv", type=("build", "run"))
