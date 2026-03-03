# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRicegeneann(RPackage):
	"""Gene Annotation of Rice (Oryza Sativa L.spp.japonica)

	Gene annotation of rice (Oryza Sativa L.spp.japonica).
    The package is based on the annotation file from the website <http://plants.ensembl.org/Oryza_sativa/Info/Index>. 
    Input gene's name then return some information, including the from position, the end position, 
    the position type and the chromosome number.
	"""
	
	cran = "ricegeneann" 

	version("1.0.2", md5="606ea34efba317a888ef202b8b953bd8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-riceidconverter", type=("build", "run"))
