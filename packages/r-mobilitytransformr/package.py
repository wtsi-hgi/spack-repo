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

	version("1.6.0", commit="7f3073e42b4b9ec4290852ba8389df0b6f00e8b2")

	depends_on("r-msnbase", type=("build", "run"))
	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-metabocoreutils", type=("build", "run"))
	depends_on("r-spectra", type=("build", "run"))
