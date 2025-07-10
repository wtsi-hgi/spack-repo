# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsobar(RPackage):
	"""Analysis and quantitation of isobarically tagged MSMS proteomics data

	isobar provides methods for preprocessing, normalization, and report generation for the analysis of quantitative mass spectrometry proteomics data labeled with isobaric tags, such as iTRAQ and TMT. Features modules for integrating and validating PTM-centric datasets (isobar-PTM). More information on http://www.ms-isobar.org.
	"""
	
	homepage = "https://github.com/fbreitwieser/isobar"
	bioc = "isobar" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/isobar_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/isobar/isobar_1.48.0.tar.gz"]

	version("1.48.0", sha256="c70547e79b09b5fe6f7728e0082d5d8c0fd85fe4b292b7b03a1d593b7051638d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-biomart", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
