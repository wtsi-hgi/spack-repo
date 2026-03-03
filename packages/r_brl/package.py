# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrl(RPackage):
	"""Beta Record Linkage

	Implementation of the record linkage methodology proposed by Sadinle (2017) <doi:10.1080/01621459.2016.1148612>.  It handles the bipartite record linkage problem, where two duplicate-free datafiles are to be merged.
	"""
	
	homepage = "https://github.com/msadinle/BRL"
	cran = "BRL" 

	version("0.1.0", md5="62783860871ff94cac994ee8ac7e4283")

	depends_on("r@3.5:", type=("build", "run"))
