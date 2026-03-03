# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RModelstudio(RPackage):
	"""Interactive Studio for Explanatory Model Analysis

	Automate the explanatory analysis of machine learning predictive 
    models. Generate advanced interactive model explanations in the form of 
    a serverless HTML site with only one line of code. This tool is 
    model-agnostic, therefore compatible with most of the black-box predictive
    models and frameworks. The main function computes various (instance and 
    model-level) explanations and produces a customisable dashboard, which 
    consists of multiple panels for plots with their short descriptions. It is 
    possible to easily save the dashboard and share it with others. modelStudio 
    facilitates the process of Interactive Explanatory Model Analysis introduced 
    in Baniecki et al. (2023) <doi:10.1007/s10618-023-00924-w>.
	"""
	
	homepage = "https://modelstudio.drwhy.ai"
	cran = "modelStudio" 

	version("3.1.2", md5="ab31aaaf18788b18d7d1df51015b9399")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dalex@2.2.1:", type=("build", "run"))
	depends_on("r-ingredients@2.2:", type=("build", "run"))
	depends_on("r-ibreakdown@2.0.1:", type=("build", "run"))
	depends_on("r-r2d3", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
