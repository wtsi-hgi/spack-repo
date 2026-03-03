# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormfluodbf(RPackage):
	"""Cleans and Normalizes FLUOstar DBF and DAT Files

	Cleans and Normalizes FLUOstar DBF and DAT Files obtained from liposome flux assays. Users should verify extended usage of the package on files from other assay types.
	"""
	
	homepage = "https://github.com/AlphaPrime7/normfluodbf"
	cran = "normfluodbf" 

	version("1.5.2", md5="a554f8ebf0454ddbc42b520bdf57c576")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreign", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emojifont", type=("build", "run"))
	depends_on("r-rio", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-badger", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
