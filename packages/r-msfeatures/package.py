# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsfeatures(RPackage):
	"""Functionality for Mass Spectrometry Features

	The MsFeature package defines functionality for Mass Spectrometry features. This includes functions to group (LC-MS) features based on some of their properties, such as retention time (coeluting features), or correlation of signals across samples. This packge hence allows to group features, and its results can be used as an input for the `QFeatures` package which allows to aggregate abundance levels of features within each group. This package defines concepts and functions for base and common data types, implementations for more specific data types are expected to be implemented in the respective packages (such as e.g. `xcms`). All functionality of this package is implemented in a modular way which allows combination of different grouping approaches and enables its re-use in other R packages.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MsFeatures"
	bioc = "MsFeatures"

	version("1.16.0", commit="467deed5ecee7a09dc79f5172f6c9299d8a84005")
	version("1.10.0", commit="206e190bb7e032bd9235db5a3beaef6a40ef88fc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-protgenerics@1.23.5:", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
