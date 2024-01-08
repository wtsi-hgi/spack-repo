# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RDocopt(RPackage):
	"""Command-Line Interface Specification Language

	Define a command-line interface by just giving it
    a description in the specific format.
	"""
	
	homepage = "https://github.com/docopt/docopt.R"
	cran = "docopt" 

	version("0.7.1", md5="97952edaf3093ed9801bd2eb1c557923")
