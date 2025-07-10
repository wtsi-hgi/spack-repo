# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSdams(RPackage):
	"""Differential Abundant/Expression Analysis for Metabolomics, Proteomics and single-cell RNA sequencing Data

	This Package utilizes a Semi-parametric Differential Abundance/expression analysis (SDA) method for metabolomics and proteomics data from mass spectrometry as well as single-cell RNA sequencing data. SDA is able to robustly handle non-normally distributed data and provides a clear quantification of the effect size.
	"""
	
	bioc = "SDAMS" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SDAMS_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SDAMS/SDAMS_1.22.0.tar.gz"]

	version("1.22.0", sha256="dec80a4e2c92f8062ced8e1fa9b773cbfda56eeb1393bc0ff137034f698eb252")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
