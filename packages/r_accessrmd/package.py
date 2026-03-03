# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccessrmd(RPackage):
	"""Improving the Accessibility of 'rmarkdown' Documents

	Provides a simple method to improve the accessibility of
    'rmarkdown' documents. The package provides functions for creating or
    modifying 'rmarkdown' documents, resolving known errors and alerts that
    result in accessibility issues for screen reader users.
	"""
	
	cran = "accessrmd" 

	version("1.0.0", md5="d79327b1af3ad2ad4d6f74eb3792cd19")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-htmltools", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
