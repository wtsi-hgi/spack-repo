# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrunch(RPackage):
	"""Crunch.io Data Tools

	The Crunch.io service <https://crunch.io/> provides a cloud-based
    data store and analytic engine, as well as an intuitive web interface.
    Using this package, analysts can interact with and manipulate Crunch
    datasets from within R. Importantly, this allows technical researchers to
    collaborate naturally with team members, managers, and clients who prefer a
    point-and-click interface.
	"""
	
	homepage = "https://crunch.io/r/crunch/"
	cran = "crunch" 

	version("1.30.4", md5="a612fae017385a791c8e7fa6508e9444")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-httr@1:", type=("build", "run"))
	depends_on("r-httpcache@0.1.4:", type=("build", "run"))
	depends_on("r-jsonlite@0.9.15:", type=("build", "run"))
