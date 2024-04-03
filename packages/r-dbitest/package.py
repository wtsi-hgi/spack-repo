# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDbitest(RPackage):
	"""Testing DBI Backends

	A helper that tests DBI back ends for conformity to the
    interface.
	"""
	
	homepage = "https://dbitest.r-dbi.org"
	cran = "DBItest" 

	version("1.8.0", md5="c30ed34e11c4e2e44ecb051fad564b66")
	version("1.8.1", md5="4c364d7e113a1ed755412a9601c4be00")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-blob@1.2:", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-dbi@1.2.1:", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-hms@0.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-nanoarrow", type=("build", "run"))
	depends_on("r-palmerpenguins", type=("build", "run"))
	depends_on("r-rlang@0.2:", type=("build", "run"))
	depends_on("r-testthat@2:", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
