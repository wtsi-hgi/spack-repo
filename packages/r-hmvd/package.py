# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHmvd(RPackage):
	"""Group Association Test using a Hidden Markov Model

	Perform association test between a group of variable and the outcome. 
	"""
	
	cran = "HMVD" 

	version("1.0", md5="444ca7be82151147b8dc4969e6c19a79")

	depends_on("r-mass", type=("build", "run"))
