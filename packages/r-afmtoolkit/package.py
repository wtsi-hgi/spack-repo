# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfmtoolkit(RPackage):
	"""Functions for Atomic Force Microscope Force-Distance Curves
Analysis

	Set of functions for analyzing Atomic Force Microscope (AFM) force-distance curves. It allows to obtain the contact and unbinding points, perform the baseline correction, estimate the Young's modulus, fit up to two exponential decay function to a stress-relaxation / creep experiment, obtain adhesion energies. These operations can be done either over a single F-d curve or over a set of F-d curves in batch  mode.
	"""
	
	cran = "afmToolkit" 

	version("0.0.1", md5="dc2e959818329114e455c11b0e3da29d")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
