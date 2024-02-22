# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConfusiontabler(RPackage):
	"""Confusion Matrix Toolset

	Takes the outputs of a 'caret' confusion matrix and allows for the quick conversion of these list items to lists.
    The intended usage is to allow the tool to work with the outputs of machine learning classification models. 
    This tool works with classification problems for binary and multi-classification problems and allows for the record level conversion of the confusion matrix outputs.
    This is useful, as it allows quick conversion of these objects for storage in database systems and to track ML model performance over time.
    Traditionally, this approach has been used for highlighting model representation and feature slippage. 
	"""
	
	cran = "ConfusionTableR" 

	version("1.0.4", md5="53194c6b378a3080c7a8f60c81e1f3bc")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-furrr", type=("build", "run"))
