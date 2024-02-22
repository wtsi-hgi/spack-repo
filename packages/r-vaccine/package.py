# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaccine(RPackage):
	"""Statistical Tools for Immune Correlates Analysis of Vaccine
Clinical Trial Data

	Various semiparametric and nonparametric statistical tools for
    immune correlates analysis of vaccine clinical trial data. This includes
    calculation of summary statistics and estimation of risk, vaccine efficacy,
    controlled effects (controlled risk and controlled vaccine efficacy), and
    mediation effects (natural direct effect, natural indirect effect,
    proportion mediated). See Gilbert P, Fong Y, Kenny A, and Carone, M (2022)
    <doi:10.1093/biostatistics/kxac024> and Fay MP and Follmann DA (2023)
    <doi:10.48550/arXiv.2208.06465>.
	"""
	
	homepage = "https://github.com/Avi-Kenny/vaccine"
	cran = "vaccine" 

	version("1.2.1", md5="67191af2b4bd61e3bcf6a0d45f5f61d2")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-fdrtool@1.2.17:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-ggpubr@0.5:", type=("build", "run"))
	depends_on("r-rlang@1.0.6:", type=("build", "run"))
	depends_on("r-rsolnp@1.16:", type=("build", "run"))
	depends_on("r-simest@0.4:", type=("build", "run"))
	depends_on("r-superlearner@2.0.28:", type=("build", "run"))
	depends_on("r-survival@3.4:", type=("build", "run"))
	depends_on("r-survml@0.0.0.9000:", type=("build", "run"))
	depends_on("r-truncnorm@1.0.8:", type=("build", "run"))
	depends_on("r-e1071@1.7.12:", type=("build", "run"))
	depends_on("r-gam@1.22.3:", type=("build", "run"))
	depends_on("r-ranger@0.16:", type=("build", "run"))
