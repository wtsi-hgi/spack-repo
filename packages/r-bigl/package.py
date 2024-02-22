# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigl(RPackage):
	"""Biochemically Intuitive Generalized Loewe Model

	Response surface methods for drug synergy analysis. Available
    methods include generalized and classical Loewe formulations as well as Highest
    Single Agent methodology. Response surfaces can be plotted in an interactive
    3-D plot and formal statistical tests for presence of synergistic effects are
    available. Implemented methods and tests are described in the article 
    "BIGL: Biochemically Intuitive Generalized Loewe null model for prediction 
    of the expected combined effect compatible with partial agonism and antagonism"
    by Koen Van der Borght, Annelies Tourny, Rytis Bagdziunas, Olivier Thas, 
    Maxim Nazarov, Heather Turner, Bie Verbist & Hugo Ceulemans (2017) 
    <doi:10.1038/s41598-017-18068-5>.
	"""
	
	homepage = "https://github.com/openanalytics/BIGL"
	cran = "BIGL" 

	version("1.9.0", md5="2e4ef57f40a5022bc94cd603b7fbbc5f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-minpack-lm", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
