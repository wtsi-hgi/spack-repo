# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCombiroc(RPackage):
	"""Selection and Ranking of Omics Biomarkers Combinations Made Easy

	Provides functions and a workflow to easily and powerfully calculating specificity, sensitivity and ROC curves of biomarkers combinations. Allows to rank and select multi-markers signatures as well as to find the best performing sub-signatures, now also from single-cell RNA-seq datasets. The method used was first published as a Shiny app and described in Mazzara et al. (2017) <doi:10.1038/srep45477> and further described in Bombaci & Rossi (2019) <doi:10.1007/978-1-4939-9164-8_16>, and widely expanded as a package as presented in the bioRxiv pre print Ferrari et al. <doi:10.1101/2022.01.17.476603>.
	"""
	
	homepage = "https://doi.org/10.1101/2022.01.17.476603"
	cran = "combiroc" 

	version("0.3.4", md5="cf340fbf2b024ca751528be782de7321")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
