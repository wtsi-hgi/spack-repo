# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpisensr(RPackage):
	"""Basic Sensitivity Analysis of Epidemiological Results

	Basic sensitivity analysis of the observed relative risks adjusting
    for unmeasured confounding and misclassification of the
    exposure/outcome, or both. It follows the bias analysis methods and
    examples from the book by Lash T.L, Fox M.P, and Fink A.K.
    "Applying Quantitative Bias Analysis to Epidemiologic Data",
    ('Springer', 2021).
	"""
	
	homepage = "https://github.com/dhaine/episensr"
	cran = "episensr" 

	version("1.3.0", md5="bb57c00e94199184527de9e738b9a022")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-triangle", type=("build", "run"))
	depends_on("r-trapezoid", type=("build", "run"))
	depends_on("r-actuar", type=("build", "run"))
	depends_on("r-dagitty", type=("build", "run"))
	depends_on("r-ggdag", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
