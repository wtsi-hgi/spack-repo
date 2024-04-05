# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RViralx(RPackage):
	"""Explainers for Regression Models in HIV Research

	A dedicated viral-explainer model tool designed to empower researchers in the field of HIV research, particularly in viral load and CD4 (Cluster of Differentiation 4) lymphocytes regression modeling. Drawing inspiration from the 'tidymodels' framework for rigorous model building of Max Kuhn and Hadley Wickham (2020) <https://www.tidymodels.org>, and the 'DALEXtra' tool for explainability by Przemyslaw Biecek (2020) <arXiv:2009.13248>. It aims to facilitate interpretable and reproducible research in biostatistics and computational biology for the benefit of understanding HIV dynamics.
	"""
	
	cran = "viralx" 

	version("1.3.0", md5="e9d0df23906a0e72c7bd06e20bc5e033")
	version("1.2.0", md5="52203fe4727f96183198ec178cc99fc7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dalex", type=("build", "run"))
	depends_on("r-dalextra", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-kknn", type=("build", "run"))
	depends_on("r-parsnip", type=("build", "run"))
	depends_on("r-plotmo", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-recipes", type=("build", "run"))
	depends_on("r-rsample", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-vdiffr", type=("build", "run"))
	depends_on("r-workflows", type=("build", "run"))
