# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPak(RPackage):
	"""Another Approach to Package Installation

	The goal of 'pak' is to make package installation faster and
    more reliable. In particular, it performs all HTTP operations in
    parallel, so metadata resolution and package downloads are fast.
    Metadata and package files are cached on the local disk as well. 'pak'
    has a dependency solver, so it finds version conflicts before
    performing the installation. This version of 'pak' supports CRAN,
    'Bioconductor' and 'GitHub' packages as well.
	"""
	
	homepage = "https://pak.r-lib.org/"
	cran = "pak" 

	version("0.7.1", md5="bc95a3a8966b8042d0201729e7ab186f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
