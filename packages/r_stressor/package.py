# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStressor(RPackage):
	"""Algorithms for Testing Models under Stress

	Traditional model evaluation metrics fail to capture model 
    performance under less than ideal conditions. This package employs 
    techniques to evaluate models "under-stress". This includes testing 
    models' extrapolation ability, or testing accuracy on specific 
    sub-samples of the overall model space. Details describing stress-testing 
    methods in this package are provided in 
    Haycock (2023) <doi:10.26076/2am5-9f67>. The other primary contribution of 
    this package is provided to R users access to the 'Python' library 'PyCaret'
    <https://pycaret.org/> for quick and easy access to auto-tuned 
    machine learning models. 
	"""
	
	cran = "stressor" 

	version("0.1.0", md5="3a9cdaa18217d6e17ce49879c647fa7a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("python@3.8.10:", type=("build", "link", "run"))
