# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROrdr(RPackage):
	"""A 'tidyverse' Extension for Ordinations and Biplots

	Ordination comprises several multivariate exploratory and
    explanatory techniques with theoretical foundations in geometric data
    analysis; see Podani (2000, ISBN:90-5782-067-6) for techniques and
    applications and Le Roux & Rouanet (2005) <doi:10.1007/1-4020-2236-0> for
    foundations.
    Greenacre (2010, ISBN:978-84-923846) shows how the most established of
    these, including principal components analysis, correspondence analysis,
    multidimensional scaling, factor analysis, and discriminant analysis,
    rely on eigen-decompositions or singular value decompositions of
    pre-processed numeric matrix data.
    These decompositions give rise to a set of shared coordinates along which
    the row and column elements can be measured. The overlay of their
    scatterplots on these axes, introduced by Gabriel (1971)
    <doi:10.1093/biomet/58.3.453>, is called a biplot.
    'ordr' provides inspection, extraction, manipulation, and visualization
    tools for several popular ordination classes supported by a set of recovery
    methods. It is inspired by and designed to integrate into 'tidyverse'
    workflows provided by Wickham et al (2019) <doi:10.21105/joss.01686>.
	"""
	
	homepage = "https://github.com/corybrunson/ordr"
	cran = "ordr" 

	version("0.1.1", md5="1ff8e67c5d7d118f4db61beeed9fc25f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-generics", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-labeling", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
