# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RPingr(RPackage):
	"""Check if a Remote Computer is Up

	Check if a remote computer is up. It can either
    just call the system ping command, or check a specified
    TCP port.
	"""
	
	homepage = "https://github.com/r-lib/pingr#readme"
	cran = "pingr" 

	version("2.0.2", md5="04c4f1b8c209dd395d37b41453432e4e")

	depends_on("r-processx", type=("build", "run"))
