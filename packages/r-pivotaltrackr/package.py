# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPivotaltrackr(RPackage):
	"""A Client for the 'Pivotal Tracker' API

	'Pivotal Tracker' <https://www.pivotaltracker.com> is a project
    management software-as-a-service that provides a REST API. This package
    provides an R interface to that API, allowing you to query it and work with
    its responses.
	"""
	
	homepage = "https://enpiar.com/r/pivotaltrackR/"
	cran = "pivotaltrackR" 

	version("0.2.0", md5="9e9984ae735deadc6b8497861232e9ba")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
