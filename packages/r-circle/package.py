# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCircle(RPackage):
	"""R Client Package for Circle CI

	Tools for interacting with the 'Circle CI' API
    (<https://circleci.com/docs/api/v2/>). Besides executing common tasks
    such as querying build logs and restarting builds, this package also
    helps setting up permissions to deploy from builds.
	"""
	
	homepage = "https://docs.ropensci.org/circle/"
	cran = "circle" 

	version("0.7.2", md5="e4f61bab6c5558cd950e4a56990d7052")

	depends_on("r-cli@2:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
