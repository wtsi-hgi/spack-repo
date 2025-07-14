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

	version("1.28.0", commit="55e1c3947d09f1a96417d5b5b0e81ed847dd1082")
	version("1.22.0", commit="45ec40e10f142a5c4b134fe0e274c5e9acc83025")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-trust", type=("build", "run"))
	depends_on("r-qvalue", type=("build", "run"))
