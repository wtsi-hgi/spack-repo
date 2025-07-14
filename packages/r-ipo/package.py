# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpo(RPackage):
	"""Automated Optimization of XCMS Data Processing parameters

	The outcome of XCMS data processing strongly depends on the parameter settings. IPO (`Isotopologue Parameter Optimization`) is a parameter optimization tool that is applicable for different kinds of samples and liquid chromatography coupled to high resolution mass spectrometry devices, fast and free of labeling steps. IPO uses natural, stable 13C isotopes to calculate a peak picking score. Retention time correction is optimized by minimizing the relative retention time differences within features and grouping parameters are optimized by maximizing the number of features showing exactly one peak from each injection of a pooled sample. The different parameter settings are achieved by design of experiment. The resulting scores are evaluated using response surface models.
	"""
	
	homepage = "https://github.com/rietho/IPO"
	bioc = "IPO"

	version("1.34.0", commit="648044388933b50ecf7ed0466b1a9f869cca7468")
	version("1.28.0", commit="b8fc7118a98be165d482a7a2d059ee76f6c6c61a")

	depends_on("r-xcms@1.50:", type=("build", "run"))
	depends_on("r-rsm", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
