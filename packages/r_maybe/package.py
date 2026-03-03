# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMaybe(RPackage):
	"""The Maybe Monad

	
    The maybe type represents the possibility of some value or nothing. 
    It is often used instead of throwing an error or returning `NULL`.
    The advantage of using a maybe type over `NULL` is that it is both composable 
    and requires the developer to explicitly acknowledge the potential absence 
    of a value, helping to avoid the existence of unexpected behaviour.
	"""
	
	homepage = "https://github.com/armcn/maybe"
	cran = "maybe" 

	version("1.1.0", md5="4ff98e1370bba7e1f150395c401d6a68")

	depends_on("r-magrittr", type=("build", "run"))
