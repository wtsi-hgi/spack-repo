# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKmunicate(RPackage):
	"""KMunicate-Style Kaplan–Meier Plots

	Produce Kaplan–Meier plots in the style recommended
    following the KMunicate study by Morris et al. (2019)
    <doi:10.1136/bmjopen-2019-030215>. The KMunicate style consists of
    Kaplan-Meier curves with confidence intervals to quantify uncertainty
    and an extended risk table (per treatment arm) depicting the number of
    study subjects at risk, events, and censored observations over time.
    The resulting plots are built using 'ggplot2' and can be further
    customised to a certain extent, including themes, fonts, and colour
    scales.
	"""
	
	homepage = "https://ellessenne.github.io/KMunicate-package/"
	cran = "KMunicate" 

	version("0.2.4", md5="f17189794e4d24bc9c7708077db6ae24")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pammtools", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
