# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChemospec(RPackage):
	"""Exploratory Chemometrics for Spectroscopy

	A collection of functions for top-down exploratory data analysis
    of spectral data including nuclear magnetic resonance (NMR), infrared (IR),
    Raman, X-ray fluorescence (XRF) and other similar types of spectroscopy.
    Includes functions for plotting and inspecting spectra, peak alignment,
    hierarchical cluster analysis (HCA), principal components analysis (PCA) and
    model-based clustering. Robust methods appropriate for this type of
    high-dimensional data are available. ChemoSpec is designed for structured
    experiments, such as metabolomics investigations, where the samples fall into
    treatment and control groups. Graphical output is formatted consistently for
    publication quality plots. ChemoSpec is intended to be very user friendly and
    to help you get usable results quickly. A vignette covering typical operations
    is available.
	"""
	
	homepage = "https://bryanhanson.github.io/ChemoSpec/"
	cran = "ChemoSpec" 

	version("6.1.10", md5="4475e9394e16897f82abd2202648f090")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-chemospecutils@1:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-readjdx@0.6:", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
