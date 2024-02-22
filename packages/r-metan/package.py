# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetan(RPackage):
	"""Multi Environment Trials Analysis

	Performs stability analysis of multi-environment trial data
    using parametric and non-parametric methods. Parametric methods
    includes Additive Main Effects and Multiplicative Interaction (AMMI)
    analysis by Gauch (2013) <doi:10.2135/cropsci2013.04.0241>, Ecovalence
    by Wricke (1965), Genotype plus Genotype-Environment (GGE) biplot
    analysis by Yan & Kang (2003) <doi:10.1201/9781420040371>, geometric
    adaptability index by Mohammadi & Amri (2008)
    <doi:10.1007/s10681-007-9600-6>, joint regression analysis by Eberhart
    & Russel (1966) <doi:10.2135/cropsci1966.0011183X000600010011x>,
    genotypic confidence index by Annicchiarico (1992), Murakami & Cruz's
    (2004) method, power law residuals (POLAR) statistics by Doring et al.
    (2015) <doi:10.1016/j.fcr.2015.08.005>, scale-adjusted coefficient of
    variation by Doring & Reckling (2018) <doi:10.1016/j.eja.2018.06.007>,
    stability variance by Shukla (1972) <doi:10.1038/hdy.1972.87>,
    weighted average of absolute scores by Olivoto et al. (2019a)
    <doi:10.2134/agronj2019.03.0220>, and multi-trait stability index by
    Olivoto et al. (2019b) <doi:10.2134/agronj2019.03.0221>.
    Non-parametric methods includes superiority index by Lin & Binns
    (1988) <doi:10.4141/cjps88-018>, nonparametric measures of phenotypic
    stability by Huehn (1990)
    <https://link.springer.com/article/10.1007/BF00024241>, TOP third
    statistic by Fox et al. (1990) <doi:10.1007/BF00040364>. Functions for
    computing biometrical analysis such as path analysis, canonical
    correlation, partial correlation, clustering analysis, and tools for
    inspecting, manipulating, summarizing and plotting typical
    multi-environment trial data are also provided.
	"""
	
	homepage = "https://github.com/TiagoOlivoto/metan"
	cran = "metan" 

	version("1.18.0", md5="6dfd78f2cffbef10a096b0d1dfa3a669")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.4.11:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
