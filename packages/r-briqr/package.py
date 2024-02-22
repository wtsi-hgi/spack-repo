# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBriqr(RPackage):
	"""Interface to the 'Briq' API

	An interface to the 'Briq' API <https://briq.github.io>. 'Briq' is
    a tool that aims to promote employee engagement by helping employees
    recognize and reward each other. Employees can praise and thank one another
    (for achieving a company goal, for example) by giving virtual credits (known
    as 'briqs' or 'bqs') that can be redeemed for various rewards. The 'Briq'
    API lets you create, read, update and delete users, user groups,
    transactions and messages. This package provides functions that simplify
    getting the users, user groups and transactions of your organization into R.
	"""
	
	cran = "briqr" 

	version("0.1.0", md5="6a06684702048ca37a0366334eb87741")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-jsonlite@1.6:", type=("build", "run"))
	depends_on("r-tibble@2.1.1:", type=("build", "run"))
