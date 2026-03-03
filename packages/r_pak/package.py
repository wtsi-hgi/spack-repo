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

	version("0.7.2", md5="b90bf9353c390d36f8d0ff9a58188a3c")
	version("0.7.1", md5="9eddae8f9345c4e5ad3a9692be09e6f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
