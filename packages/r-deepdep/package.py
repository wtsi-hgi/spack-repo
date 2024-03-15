# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepdep(RPackage):
	"""Visualise and Explore the Deep Dependencies of R Packages

	Provides tools for exploration of R package dependencies. 
    The main deepdep() function allows to acquire deep dependencies of any package and plot them in an elegant way.
    It also adds some popularity measures for the packages e.g. in the form of download count through the 'cranlogs' package. 
    Uses the CRAN metadata database <http://crandb.r-pkg.org> and Bioconductor metadata <https://bioconductor.org>.
    Other data acquire functions are: get_dependencies(), get_downloads() and get_description(). 
    The deepdep_shiny() function runs shiny application that helps to produce a nice 'deepdep' plot. 
	"""
	
	homepage = "https://dominikrafacz.github.io/deepdep/"
	cran = "deepdep" 

	version("0.4.3", md5="58e42d792ac9bb5d055bf152704d28b7")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-cranlogs", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
