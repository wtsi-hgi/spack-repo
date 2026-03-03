# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMm2sdata(RPackage):
	"""Gene Expression Datasets for the 'MM2S' Package

	Gene Expression datasets for the 'MM2S' package. Contains normalized expression data for Human Medulloblastoma ('GSE37418') as well as Mouse Medulloblastoma models ('GSE36594'). Deena Gendoo et al. (2015) <doi:10.1016/j.ygeno.2015.05.002>.
	"""
	
	cran = "MM2Sdata" 

	version("1.0.3", md5="8717aabe857695f8bd63333f45c79643")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
