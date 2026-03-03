# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrocontax(RPackage):
	"""The ConTax Data Package

	The consensus taxonomy for prokaryotes is a set of data-sets for
    best possible taxonomic classification based on 16S rRNA sequence data.
	"""
	
	cran = "microcontax" 

	version("1.2", md5="65ff93163f0ff6f41394c791dbc1254c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-microseq", type=("build", "run"))
