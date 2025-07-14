# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRforproteomics(RPackage):
	"""Companion package to the 'Using R and Bioconductor for proteomics data analysis' publication

	This package contains code to illustrate the 'Using R and Bioconductor for proteomics data analysis' and 'Visualisation of proteomics data using R and Bioconductor' manuscripts. The vignettes describe the code and data needed to reproduce the examples and figures described in the paper and functionality for proteomics visualisation. It also contain various function to discover R software for mass spectrometry and proteomics.
	"""
	
	homepage = "http://lgatto.github.com/RforProteomics/"
	bioc = "RforProteomics" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/RforProteomics_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/RforProteomics/RforProteomics_1.40.0.tar.gz"]

    version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="bd594566d574d592604245bfd226e14a7d452b26f6640e1c7520133037a49285")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msnbase@2.5.3:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-biocviews", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))

