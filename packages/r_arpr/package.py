# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArpr(RPackage):
	"""Advanced R Pipes

	Provides convenience functions for programming with
    'magrittr' pipes. Conditional pipes, a string prefixer and a function
    to pipe the given object into a specific argument given by character
    name are currently supported. It is named after the dadaist Hans Arp,
    a friend of Rene Magritte.
	"""
	
	homepage = "https://github.com/statnmap/arpr"
	cran = "arpr" 

	version("0.1.2", md5="00e540f002896af51df2b61a2c63a729")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
