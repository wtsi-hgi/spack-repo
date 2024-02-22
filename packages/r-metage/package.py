# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetage(RPackage):
	"""Meta-Analysis for Detecting Genotype x Environment Associations

	Meta-analysis of genome-wide association studies for studying
    Genotype x Environment interactions.  The 4 main functions of the
    package metaGE.collect(), metaGE.cor(), metaGE.fit() and metaGE.test()
    correspond to 4 steps to perform the meta-analysis: Collecting the
    results of genome-wide association studies data from different files;
    Inferring the inter-environment correlation matrix; Performing global
    test procedure for quantitative trait loci detection (using a Fixed or
    Random effect model); Performing tests of contrast or meta-regression
    using an environmental co-factor. (De Walsche, A., et al. (2023)
    <doi:10.1101/2023.03.01.530237>).
	"""
	
	cran = "metaGE" 

	version("1.0.3", md5="2d94fa99f7589f85fc04319c60174015")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-corrplot", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-emdbook", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ks", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-qqman", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
