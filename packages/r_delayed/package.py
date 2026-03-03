# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDelayed(RPackage):
	"""A Framework for Parallelizing Dependent Tasks

	Mechanisms to parallelize dependent tasks in a manner that
    optimizes the compute resources available. It provides access to "delayed"
    computations, which may be parallelized using futures. It is, to an extent,
    a facsimile of the 'Dask' library (<https://www.dask.org/>), for the 'Python'
    language.
	"""
	
	homepage = "https://tlverse.org/delayed/"
	cran = "delayed" 

	version("0.4.0", md5="0e6362cfe115f8566aaaa0c50cba6418")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-rstackdeque", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-visnetwork", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-bbmisc", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-r-oo", type=("build", "run"))
