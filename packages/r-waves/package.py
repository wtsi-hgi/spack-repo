# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaves(RPackage):
	"""Vis-NIR Spectral Analysis Wrapper

	Originally designed application in the context of
    resource-limited plant research and breeding programs, 'waves'
    provides an open-source solution to spectral data processing and model
    development by bringing useful packages together into a streamlined
    pipeline.  This package is wrapper for functions related to the
    analysis of point visible and near-infrared reflectance measurements.
    It includes visualization, filtering, aggregation, preprocessing,
    cross-validation set formation, model training, and prediction
    functions to enable open-source association of spectral and reference
    data. This package is documented in a peer-reviewed manuscript in the
    Plant Phenome Journal <doi:10.1002/ppj2.20012>.  Specialized
    cross-validation schemes are described in detail in Jarquín et al.
    (2017) <doi:10.3835/plantgenome2016.12.0130>. Example data is from
    Ikeogu et al. (2017) <doi:10.1371/journal.pone.0188918>.
	"""
	
	homepage = "https://github.com/GoreLab/waves"
	cran = "waves" 

	version("0.2.5", md5="4aa864a9b5ffab5b3efe0dd47b746c58")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-prospectr", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-spectacles", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
