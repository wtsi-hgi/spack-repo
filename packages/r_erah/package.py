# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErah(RPackage):
	"""Automated Spectral Deconvolution, Alignment, and Metabolite
Identification in GC/MS-Based Untargeted Metabolomics

	Automated compound deconvolution, alignment across samples, and identification of metabolites by spectral library matching in Gas Chromatography - Mass spectrometry (GC-MS) untargeted metabolomics. Outputs a table with compound names, matching scores and the integrated area of the compound for each sample. Package implementation is described in Domingo-Almenara et al. (2016) <doi:10.1021/acs.analchem.6b02927>.
	"""
	
	homepage = "http://metsyslab.com/"
	cran = "erah" 

	version("2.0.1", md5="b140866e054d2de8a5b3640da44aa79d")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-osd", type=("build", "run"))
	depends_on("r-hiclimr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
