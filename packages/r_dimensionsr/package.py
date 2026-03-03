# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDimensionsr(RPackage):
	"""Gathering Bibliographic Records from 'Digital Science
Dimensions' Using 'DSL' API

	A set of tools to extract bibliographic content from 'Digital Science Dimensions' using 'DSL' API <https://www.dimensions.ai/dimensions-apis/>.
	"""
	
	homepage = "https://github.com/massimoaria/dimensionsR"
	cran = "dimensionsR" 

	version("0.0.3", md5="0cbbb2ab55c7ab2cede081d2b524bada")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
