# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNormalize450k(RPackage):
	"""Preprocessing of Illumina Infinium 450K data

	Precise measurements are important for epigenome-wide studies investigating DNA methylation in whole blood samples, where effect sizes are expected to be small in magnitude. The 450K platform is often affected by batch effects and proper preprocessing is recommended. This package provides functions to read and normalize 450K '.idat' files. The normalization corrects for dye bias and biases related to signal intensity and methylation of probes using local regression. No adjustment for probe type bias is performed to avoid the trade-off of precision for accuracy of beta-values.
	"""
	
	bioc = "normalize450K" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/normalize450K_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/normalize450K/normalize450K_1.30.0.tar.gz"]

	version("1.30.0", md5="f5ea0fdcbdd43103b5ee941c96fe43fa")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
