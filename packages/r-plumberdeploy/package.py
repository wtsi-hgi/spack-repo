# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlumberdeploy(RPackage):
	"""Plumber Deployment

	Gives the ability to automatically deploy a plumber API
    from R functions on 'DigitalOcean' and other cloud-based servers.
	"""
	
	homepage = "https://github.com/meztez/plumberDeploy"
	cran = "plumberDeploy" 

	version("0.2.1", md5="82a1c971b3a38dd2e5d3c30e630075a8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-analogsea@0.9.4:", type=("build", "run"))
	depends_on("r-ssh", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("libssh", type=("build", "link", "run"))
