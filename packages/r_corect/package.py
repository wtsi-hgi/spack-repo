# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorect(RPackage):
	"""Programmatic Analysis of Sediment Cores Using Computed
Tomography Imaging

	Computed tomography (CT) imaging is a powerful tool for understanding the composition of sediment cores. This package streamlines and accelerates the analysis of CT data generated in the context of environmental science. Included are tools for processing raw DICOM images to characterize sediment composition (sand, peat, etc.). Root analyses are also enabled, including measures of external surface area and volumes for user-defined root size classes. For a detailed description of the application of computed tomography imaging for sediment characterization, see: Davey, E., C. Wigand, R. Johnson, K. Sundberg, J. Morris, and C. Roman. (2011) <DOI: 10.1890/10-2037.1>.
	"""
	
	homepage = "https://github.com/troyhill/coreCT"
	cran = "coreCT" 

	version("1.3.3", md5="f1ba899c75f37b3f002f281a9302818a")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-oro-dicom", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
