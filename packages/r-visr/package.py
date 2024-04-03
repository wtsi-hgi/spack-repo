# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisr(RPackage):
	"""Clinical Graphs and Tables Adhering to Graphical Principles

	To enable fit-for-purpose, reusable clinical and medical
    research focused visualizations and tables with sensible defaults and
    based on graphical principles as described in: "Vandemeulebroecke et
    al. (2018)" <doi:10.1002/pst.1912>, "Vandemeulebroecke et al. (2019)"
    <doi:10.1002/psp4.12455>, and "Morris et al. (2019)"
    <doi:10.1136/bmjopen-2019-030215>.
	"""
	
	homepage = "https://openpharma.github.io/visR/"
	cran = "visR" 

	version("0.4.1", md5="a14d4afd0c9fdc26565ddf794322d16a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-broom@0.7.11:", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-forcats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gt@0.3:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-survival@3.4.0:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidycmprsk@0.1.1:", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
