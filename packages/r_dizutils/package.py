# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDizutils(RPackage):
	"""Utilities for 'DIZ' R Package Development

	Utility functions used for the R package development
    infrastructure inside the data integration centers ('DIZ') to
    standardize and facilitate repetitive tasks such as setting up a
    database connection or issuing notification messages and to avoid
    redundancy.
	"""
	
	homepage = "https://github.com/miracum/misc-dizutils"
	cran = "DIZutils" 

	version("0.1.2", md5="aae5ad01dcdbaf6a12c5ad50bb2af108")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbi@1.1:", type=("build", "run"))
	depends_on("r-diztools", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-rjdbc", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rpostgres", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("postgresql@9.0:+client_only", type=("build", "link", "run"))
