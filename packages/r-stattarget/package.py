# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStattarget(RPackage):
	"""Statistical Analysis of Molecular Profiles

	A streamlined tool provides a graphical user interface for quality control based signal drift correction (QC-RFSC), integration of data from multi-batch MS-based experiments, and the comprehensive statistical analysis in metabolomics and proteomics.
	"""
	
	homepage = "https://stattarget.github.io"
	bioc = "statTarget"

	version("1.38.0", commit="d67f95a82c5fa1509ef5d599003a7c0d40342ea4")
	version("1.32.0", commit="bbfcb6154aaa861f2174a51179303676e6f63287")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-pdist", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
