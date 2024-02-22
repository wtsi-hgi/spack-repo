# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamiliar(RPackage):
	"""End-to-End Automated Machine Learning and Model Evaluation

	Single unified interface for end-to-end modelling of regression, 
    categorical and time-to-event (survival) outcomes. Models created using
    familiar are self-containing, and their use does not require additional
    information such as baseline survival, feature clustering, or feature
    transformation and normalisation parameters. Model performance,
    calibration, risk group stratification, (permutation) variable importance,
    individual conditional expectation, partial dependence, and more, are
    assessed automatically as part of the evaluation process and exported in
    tabular format and plotted, and may also be computed manually using export
    and plot functions. Where possible, metrics and values obtained during the
    evaluation process come with confidence intervals.
	"""
	
	homepage = "https://github.com/alexzwanenburg/familiar"
	cran = "familiar" 

	version("1.4.6", md5="71254d436092e8d8743576195d9b4813")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang@0.3.4:", type=("build", "run"))
	depends_on("r-rstream", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
