# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBhm(RPackage):
	"""Biomarker Threshold Models

	Contains tools to fit both predictive and prognostic biomarker effects using biomarker threshold models and continuous threshold models. Evaluate the treatment effect, biomarker effect and treatment-biomarker interaction using probability index measurement. Test for treatment-biomarker interaction using residual bootstrap method.
	"""
	
	cran = "bhm" 

	version("1.18", md5="6d7a3c41ee000417cc96f3eb0e243b0d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
