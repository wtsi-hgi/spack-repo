# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeduped(RPackage):
	"""Making "Deduplicated" Functions

	Contains one main function deduped() which speeds up slow,
    vectorized functions by only performing computations on the unique values
    of the input and expanding the results at the end.
	"""
	
	homepage = "https://github.com/orgadish/deduped"
	cran = "deduped" 

	version("0.2.0", md5="dcbbd2899c52f364f86db6219e42eb91")

	depends_on("r-collapse", type=("build", "run"))
	depends_on("r-fastmatch", type=("build", "run"))
