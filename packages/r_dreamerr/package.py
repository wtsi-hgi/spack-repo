# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDreamerr(RPackage):
	"""Error Handling Made Easy

	Set of tools to facilitate package development and make R a more user-friendly place. Mostly for developers (or anyone who writes/shares functions). Provides a simple, powerful and flexible way to check the arguments passed to functions. 
    The developer can easily describe the type of argument needed. If the user provides a wrong argument, then an informative error message is prompted with the requested type and the problem clearly stated--saving the user a lot of time in debugging. 
	"""
	
	cran = "dreamerr" 

	version("1.4.0", md5="df2e0c5e9378f06e81f48a71389bb692")

	depends_on("r-formula", type=("build", "run"))
	depends_on("r-stringmagic", type=("build", "run"))
