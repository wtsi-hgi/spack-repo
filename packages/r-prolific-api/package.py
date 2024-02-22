# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProlificApi(RPackage):
	"""A User-Friendly Interface for Accessing the Prolific API

	A user-friendly interface for creating and managing empirical crowd-sourcing studies via API access to <https://www.prolific.co>. 
	"""
	
	cran = "prolific.api" 

	version("0.5.2", md5="8b99515280a133df5ac50aaed7412309")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table@1.14.6:", type=("build", "run"))
	depends_on("r-jsonlite@1.8.4:", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
