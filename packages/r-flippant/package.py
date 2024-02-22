# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlippant(RPackage):
	"""Dithionite Scramblase Assay Analysis

	The lipid scrambling activity of protein extracts and purified
    scramblases is often determined using a fluorescence-based assay involving
    many manual steps. flippant offers an integrated solution for the analysis
    and publication-grade graphical presentation of dithionite scramblase
    assays, as well as a platform for review, dissemination and extension of the
    strategies it employs. The package's name derives from a play on the fact
    that lipid scrambling is also sometimes referred to as 'flipping'.
    The package is originally published as Cotton, R.J., Ploier, B., Goren,
    M.A., Menon, A.K., and Graumann, J. (2017). "flippant–An R package for the
    automated analysis of fluorescence-based scramblase assays." BMC
    Bioinformatics 18, 146. <DOI:10.1186/s12859-017-1542-y>.
	"""
	
	cran = "flippant" 

	version("1.5.4", md5="8343e57003d42d3e38161c0071d9a20e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
	depends_on("r-assertive-base@0.0.7:", type=("build", "run"))
	depends_on("r-assertive-files@0.0.2:", type=("build", "run"))
	depends_on("r-assertive-numbers@0.0.2:", type=("build", "run"))
	depends_on("r-data-table@1.11.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-pracma@2.3.3:", type=("build", "run"))
	depends_on("r-stringi@1.2.3:", type=("build", "run"))
	depends_on("r-withr@2.1.2:", type=("build", "run"))
