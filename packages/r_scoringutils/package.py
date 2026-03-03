# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScoringutils(RPackage):
	"""Utilities for Scoring and Assessing Predictions

	
    Provides a collection of metrics and proper scoring rules 
    (Tilmann Gneiting & Adrian E Raftery (2007) 
    <doi:10.1198/016214506000001437>, Jordan, A., Krüger, F., & Lerch, S. (2019)
    <doi:10.18637/jss.v090.i12>) within a consistent framework for 
    evaluation, comparison and visualisation of forecasts. 
    In addition to proper scoring rules, functions are provided to assess 
    bias, sharpness and calibration 
    (Sebastian Funk, Anton Camacho, Adam J. Kucharski, Rachel Lowe, Rosalind
    M. Eggo, W. John Edmunds (2019) <doi:10.1371/journal.pcbi.1006785>) of 
    forecasts. 
    Several types of predictions (e.g. binary, discrete, continuous) which may 
    come in different formats (e.g. forecasts represented by predictive samples 
    or by quantiles of the predictive distribution) can be evaluated. 
    Scoring metrics can be used either through a convenient data.frame format, 
    or can be applied as individual functions in a vector / matrix format. 
    All functionality has been implemented with a focus on performance and is 
    robustly tested. Find more information about the package in the 
    accompanying paper (<doi:10.48550/arXiv.2205.07090>).
	"""
	
	homepage = "https://doi.org/10.48550/arXiv.2205.07090"
	cran = "scoringutils" 

	version("1.2.2", md5="ab6500a806a8bdcb69b416f1cc11ad84")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggdist@3.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scoringrules", type=("build", "run"))
