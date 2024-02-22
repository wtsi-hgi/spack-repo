# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncase(RPackage):
	"""Pipe-Friendly Vector Replacement with Case Statements

	Offers a pipe-friendly alternative to the 'dplyr' functions
    case_when() and if_else(), as well as a number of user-friendly
    simplifications for common use cases.  These functions accept a vector
    as an optional first argument, allowing conditional statements to be
    built using the 'magrittr' dot operator.  The functions also coerce
    all outputs to the same type, meaning you no longer have to worry
    about using specific typed variants of NA or explicitly declaring
    integer outputs, and evaluate outputs somewhat lazily, so you don't
    waste time on long operations that won't be used.
	"""
	
	homepage = "https://pkg.rossellhayes.com/incase/"
	cran = "incase" 

	version("0.3.2", md5="75183a3490f934e068e6d12d6d2da915")

	depends_on("r-backports", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-plu", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
