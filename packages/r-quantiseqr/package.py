# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQuantiseqr(RPackage):
	"""Quantification of the Tumor Immune contexture from RNA-seq data

	This package provides a streamlined workflow for the quanTIseq method, developed to perform the quantification of the Tumor Immune contexture from RNA-seq data. The quantification is performed against the TIL10 signature (dissecting the contributions of ten immune cell types), carefully crafted from a collection of human RNA-seq samples. The TIL10 signature has been extensively validated using simulated, flow cytometry, and immunohistochemistry data.
	"""
	
	bioc = "quantiseqr"

	version("1.16.0", commit="b7e6a4737761f45bbecfcb8f562ce891e633ab99")
	version("1.10.0", commit="3ea45f1a1556ad06b5bcf67fb20374df3bcdb434")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
