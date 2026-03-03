# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPotools(RPackage):
	"""Tools for Internationalization and Portability in R Packages

	Translating messages in R packages is managed using the po
    top-level directory and the 'gettext' program. This package provides
    some helper functions for building this support in R packages, e.g.
    common validation & I/O tasks.
	"""
	
	homepage = "https://github.com/MichaelChirico/potools"
	cran = "potools" 

	version("0.2.4", md5="40827db711c2742582472bd4ba7d9f8e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("gettext", type=("build", "link", "run"))
