# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCitan(RPackage):
	"""CITation ANalysis Toolpack

	Supports quantitative
    research in scientometrics and bibliometrics. Provides
    various tools for preprocessing bibliographic
    data retrieved, e.g., from Elsevier's SciVerse Scopus,
    computing bibliometric impact of individuals,
    or modelling phenomena encountered in the social sciences.
    This package is deprecated, see 'agop' instead.
	"""
	
	homepage = "https://github.com/gagolews/CITAN"
	cran = "CITAN" 

	version("2022.1.1", md5="73e51802d12797b8cf2fadb6ea72d374")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-agop", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
