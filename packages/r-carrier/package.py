# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCarrier(RPackage):
	"""Isolate Functions for Remote Execution

	Sending functions to remote processes can be wasteful of
    resources because they carry their environments with them. With the
    carrier package, it is easy to create functions that are isolated from
    their environment. These isolated functions, also called crates, print
    at the console with their total size and can be easily tested locally
    before being sent to a remote.
	"""
	
	homepage = "https://github.com/r-lib/carrier"
	cran = "carrier" 

	version("0.1.1", md5="8ab1a1c4401a87fe6174b703c978192b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-lobstr", type=("build", "run"))
	depends_on("r-rlang@1.0.1:", type=("build", "run"))
