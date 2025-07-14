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

	version("1.36.0", commit="a965574f7e6673fcc6e7418b7145bcfb574e5264")
	version("1.30.0", commit="9480566b40fbf1c0f89d5fadce4ee3e7c145971b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
