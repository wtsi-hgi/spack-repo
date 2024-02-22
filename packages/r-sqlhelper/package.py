# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSqlhelper(RPackage):
	"""Easier 'SQL' Integration

	Execute files of 'SQL' and manage database connections. 'SQL' statements and queries may be interpolated with string literals. Execution of individual statements and queries may be controlled with keywords. Multiple connections may be defined with 'YAML' and accessed by name. 
	"""
	
	homepage = "https://majerr.github.io/sqlhelper/dev/"
	cran = "sqlhelper" 

	version("0.2.1", md5="6b384fc48d905b4604ea656c39486879")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-pool", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-purrr@1:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
