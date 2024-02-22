# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDtrackr(RPackage):
	"""Track your Data Pipelines

	Track and
    document 'dplyr' data pipelines. As you filter, mutate, and join your
    way through a data set, 'dtrackr' seamlessly keeps track of your data
    flow and makes publication ready documentation of a data pipeline simple.
	"""
	
	homepage = "https://terminological.github.io/dtrackr/index.html"
	cran = "dtrackr" 

	version("0.4.4", md5="786194596e866ab738eb49e6dc01ef83")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-rsvg", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-pdftools", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
