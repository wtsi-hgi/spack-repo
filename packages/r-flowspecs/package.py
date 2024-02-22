# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowspecs(RPackage):
	"""Tools for processing of high-dimensional cytometry data

	This package is intended to fill the role of conventional cytometry pre-processing software, for spectral decomposition, transformation, visualization and cleanup, and to aid further downstream analyses, such as with DepecheR, by enabling transformation of flowFrames and flowSets to dataframes. Functions for flowCore-compliant automatic 1D-gating/filtering are in the pipe line. The package name has been chosen both as it will deal with spectral cytometry and as it will hopefully give the user a nice pair of spectacles through which to view their data.
	"""
	
	bioc = "flowSpecs" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/flowSpecs_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/flowSpecs/flowSpecs_1.16.0.tar.gz"]

	version("1.16.0", md5="502f1e04027fab8076745a5386401f2e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-biocgenerics@0.30:", type=("build", "run"))
	depends_on("r-biocparallel@1.18.1:", type=("build", "run"))
	depends_on("r-biobase@2.48:", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-flowcore@1.50:", type=("build", "run"))
	depends_on("r-zoo@1.8.6:", type=("build", "run"))
