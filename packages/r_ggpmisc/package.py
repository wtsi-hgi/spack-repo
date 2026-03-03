# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpmisc(RPackage):
	"""Miscellaneous Extensions to 'ggplot2'

	Extensions to 'ggplot2' respecting the grammar of graphics
    paradigm. Statistics: locate and tag peaks and valleys; label plot with the
    equation of a fitted polynomial or other types of models; labels
    with P-value, R^2 or adjusted R^2 or information criteria for fitted models;
    label with ANOVA table for fitted models; label with summary for fitted
    models. Model fit classes for which suitable methods are provided by package
    'broom' and 'broom.mixed' are supported. Scales and stats to build volcano
    and quadrant plots based on outcomes, fold changes, p-values and false 
    discovery rates.
	"""
	
	homepage = "https://docs.r4photobiology.info/ggpmisc/"
	cran = "ggpmisc" 

	version("0.5.5", md5="a6b7e07140e0899730b072b37dccc180")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggpp@0.5.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-scales@1.2:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-generics@0.1.2:", type=("build", "run"))
	depends_on("r-mass@7.3.51.6:", type=("build", "run"))
	depends_on("r-confintr@0.1.2:", type=("build", "run"))
	depends_on("r-polynom@1.4.0:", type=("build", "run"))
	depends_on("r-quantreg@5.93:", type=("build", "run"))
	depends_on("r-lmodel2@1.7.3:", type=("build", "run"))
	depends_on("r-splus2r@1.3.3:", type=("build", "run"))
	depends_on("r-multcomp@1.4.25:", type=("build", "run"))
	depends_on("r-multcompview@0.1.9:", type=("build", "run"))
	depends_on("r-tibble@3.1.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.6:", type=("build", "run"))
	depends_on("r-dplyr@1.0.6:", type=("build", "run"))
	depends_on("r-lubridate@1.7.10:", type=("build", "run"))
