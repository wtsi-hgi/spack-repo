# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabnorm(RPackage):
	"""Normalize Laboratory Measurements by Age and Sex

	Provides functions for normalizing standard laboratory measurements (e.g. hemoglobin, cholesterol levels) according to age and sex, based on the algorithms described in "Personalized lab test models to quantify disease potentials in healthy individuals" (Netta Mendelson Cohen, Omer Schwartzman, Ram Jaschek, Aviezer Lifshitz, Michael Hoichman, Ran Balicer, Liran I. Shlush, Gabi Barbash & Amos Tanay, <doi:10.1038/s41591-021-01468-6>). Allows users to easily obtain normalized values for standard lab results, and to visualize their distributions. See more at <https://tanaylab.weizmann.ac.il/labs/>.
	"""
	
	cran = "labNorm" 

	version("1.0.1", md5="4de6b49e0f9f679e17ba706daf92c11a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
	depends_on("r-yesno", type=("build", "run"))
