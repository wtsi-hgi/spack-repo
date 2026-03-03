# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJuliaconnector(RPackage):
	"""A Functionally Oriented Interface for Integrating 'Julia' with R

	Allows to import functions and whole packages from 'Julia' in R.
    Imported 'Julia' functions can directly be called as R functions.
    Data structures can be translated between 'Julia' and R.
    More details can also be found in the corresponding article
    <doi:10.18637/jss.v101.i06>.
	"""
	
	cran = "JuliaConnectoR" 

	version("1.1.3", md5="271bb01441723e98344d2a869b4bff20")

	depends_on("julia@1.0:", type=("build", "link", "run"))
