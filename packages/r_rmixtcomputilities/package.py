# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmixtcomputilities(RPackage):
	"""Utility Functions for 'MixtComp' Outputs

	Mixture Composer <https://github.com/modal-inria/MixtComp> is a project to build mixture models with
    heterogeneous data sets and partially missing data management. This package contains graphical, getter and some utility
    functions to facilitate the analysis of 'MixtComp' output.
	"""
	
	homepage = "https://github.com/modal-inria/MixtComp"
	cran = "RMixtCompUtilities" 

	version("4.1.6", md5="d69eadbad91b6e7611cca36422c2b709")

	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
