# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWordpredictor(RPackage):
	"""Develop Text Prediction Models Based on N-Grams

	A framework for developing n-gram models for text prediction.
    It provides data cleaning, data sampling, extracting tokens from text,
    model generation, model evaluation and word prediction. For information on how n-gram models 
    work we referred to: "Speech and Language Processing"
    <https://web.stanford.edu/~jurafsky/slp3/3.pdf>. For optimizing R code and
    using R6 classes we referred to "Advanced R" 
    <https://adv-r.hadley.nz/r6.html>. For writing R extensions we referred to 
    "R Packages", <https://r-pkgs.org/index.html>.
	"""
	
	homepage = "https://github.com/pakjiddat/word-predictor"
	cran = "wordpredictor" 

	version("0.0.3", md5="54fdf6bd0b6832b0379c75ab11f85272")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-snowballc", type=("build", "run"))
