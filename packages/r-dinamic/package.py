# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDinamic(RPackage):
	"""DiNAMIC A Method To Analyze Recurrent DNA Copy Number
Aberrations in Tumors

	This function implements the DiNAMIC procedure for
        assessing the statistical significance of recurrent DNA copy
        number aberrations (Bioinformatics (2011) 27(5) 678 - 685).
	"""
	
	cran = "dinamic" 

	version("1.0", md5="f77353caed46518fd6e1f325145eabf1")

