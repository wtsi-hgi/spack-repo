# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBloodgen3module(RPackage):
	"""This R package for performing module repertoire analyses and generating fingerprint representations

	The BloodGen3Module package provides functions for R user performing module repertoire analyses and generating fingerprint representations. Functions can perform group comparison or individual sample analysis and visualization by fingerprint grid plot or fingerprint heatmap. Module repertoire analyses typically involve determining the percentage of the constitutive genes for each module that are significantly increased or decreased. As we describe in details;https://www.biorxiv.org/content/10.1101/525709v2 and https://pubmed.ncbi.nlm.nih.gov/33624743/, the results of module repertoire analyses can be represented in a fingerprint format, where red and blue spots indicate increases or decreases in module activity. These spots are subsequently represented either on a grid, with each position being assigned to a given module, or in a heatmap where the samples are arranged in columns and the modules in rows.
	"""
	
	bioc = "BloodGen3Module" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BloodGen3Module_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BloodGen3Module/BloodGen3Module_1.10.0.tar.gz"]

	version("1.10.0", md5="c9957080f8c55f99ebcc89cdc652deb9")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
	depends_on("r-complexheatmap@1.99.8:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-v8", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
