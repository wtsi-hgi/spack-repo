# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStevedore(RPackage):
	"""Docker Client

	Work with containers over the Docker API.  Rather than
    using system calls to interact with a docker client, using the
    API directly means that we can receive richer information from
    docker.  The interface in the package is automatically generated
    using the 'OpenAPI' (a.k.a., 'swagger') specification, and all
    return values are checked in order to make them type stable.
	"""
	
	homepage = "https://github.com/richfitz/stevedore"
	cran = "stevedore" 

	version("0.9.6", md5="e31c8bb5edbf5bd72031732e66311c96")

	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl@2.3:", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-yaml@2.1.18:", type=("build", "run"))
