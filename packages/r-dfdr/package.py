# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDfdr(RPackage):
	"""Automatic Differentiation of Simple Functions

	Implementation of automatically computing derivatives
    of functions (see Mailund Thomas (2017) <doi:10.1007/978-1-4842-2881-4>). Moreover, calculating gradients, Hessian and Jacobian matrices is possible.
	"""
	
	cran = "dfdr" 

	version("0.2.0", md5="b2faa5531d36d377c3e28c8af7d438c4")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-pryr", type=("build", "run"))
