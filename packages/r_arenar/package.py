# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArenar(RPackage):
	"""Arena for the Exploration and Comparison of any ML Models

	Generates data for challenging machine learning models in 'Arena'
    <https://arena.drwhy.ai> - an interactive web application. You can start
    the server with XAI (Explainable Artificial Intelligence) plots to be
    generated on-demand or precalculate and auto-upload data file beside
    shareable 'Arena' URL.
	"""
	
	homepage = "https://arenar.drwhy.ai"
	cran = "arenar" 

	version("0.2.0", md5="3584d4349f446e63ecf1d929ff70630a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-ingredients", type=("build", "run"))
	depends_on("r-ibreakdown", type=("build", "run"))
	depends_on("r-gistr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-plumber", type=("build", "run"))
	depends_on("r-auditor", type=("build", "run"))
	depends_on("r-dalex@1.3:", type=("build", "run"))
	depends_on("r-fairmodels", type=("build", "run"))
