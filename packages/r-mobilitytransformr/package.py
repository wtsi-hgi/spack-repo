# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMobilitytransformr(RPackage):
	"""Effective mobility scale transformation of CE-MS(/MS) data

	MobilityTransformR collects a tool set for effective mobility scale transformation of CE-MS/MS data in order to increase reproducibility. It provides functionality to determine the migration times from mobility markers that have been added to the analysis and performs the transformation based on these markers. MobilityTransformR supports the conversion of numeric vectors, Spectra-objects, and MSnOnDiskExp.
	"""
	
	homepage = "https://github.com/LiesaSalzer/MobilityTransformR"
	bioc = "MobilityTransformR" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MobilityTransformR_1.6.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MobilityTransformR/MobilityTransformR_1.6.0.tar.gz"]

	version("1.6.0", md5="1d0f7904be49e25235092248b757df19")

	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-metabocoreutils", type=("build", "run"))
	depends_on("r-spectra", type=("build", "run"))
