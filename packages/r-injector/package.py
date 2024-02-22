# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInjector(RPackage):
	"""R Dependency Injection

	R dependency injection framework. Dependency injection allows
    a program design to follow the dependency inversion principle. The user
    delegates to external code (the injector) the responsibility of providing its
    dependencies. This separates the responsibilities of use and construction.
	"""
	
	homepage = "https://github.com/dfci-cccb/injectoR"
	cran = "injectoR" 

	version("0.2.4", md5="7cf24e5ce1a164e9f19d97c90ba15ac2")

	depends_on("r@3.1:", type=("build", "run"))
