# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSsh(RPackage):
	"""Secure Shell (SSH) Client for R

	Connect to a remote server over SSH to transfer files via SCP, 
    setup a secure tunnel, or run a command or script on the host while 
    streaming stdout and stderr directly to the client.
	"""
	
	homepage = "https://docs.ropensci.org/ssh/"
	cran = "ssh" 

	version("0.9.1", md5="754b4225bcdbfe977ac2319a645eef3e")

	depends_on("r-credentials", type=("build", "run"))
	depends_on("r-askpass", type=("build", "run"))
	depends_on("libssh", type=("build", "link", "run"))
