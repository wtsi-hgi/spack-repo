# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHerper(RPackage):
	"""The Herper package is a simple toolset to install and manage conda packages and environments from R

	Many tools for data analysis are not available in R, but are present in public repositories like conda. The Herper package provides a comprehensive set of functions to interact with the conda package managament system. With Herper users can install, manage and run conda packages from the comfort of their R session. Herper also provides an ad-hoc approach to handling external system requirements for R packages. For people developing packages with python conda dependencies we recommend using basilisk (https://bioconductor.org/packages/release/bioc/html/basilisk.html) to internally support these system requirments pre-hoc.
	"""
	
	homepage = "https://github.com/RockefellerUniversity/Herper"
	bioc = "Herper" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/Herper_1.12.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/Herper/Herper_1.12.0.tar.gz"]

	version("1.12.0", md5="dad437a472cae186246d3cf0f6b44964")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
