# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RManagelocalrepo(RPackage):
	"""Manage a CRAN-Style Local Repository

	This will allow easier management of a CRAN-style repository on
    local networks (i.e. not on CRAN). This might be necessary where hosted
    packages contain intellectual property owned by a corporation.
	"""
	
	cran = "managelocalrepo" 

	version("0.1.5", md5="763fc484c3b1a48255b852c91ca8f341")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-stringr@0.6.2:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
