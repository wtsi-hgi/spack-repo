# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgpval(RPackage):
	"""Annotate Statistical Tests for 'ggplot2'

	Automatically performs desired statistical tests (e.g. wilcox.test(), t.test()) to compare between groups, 
    and adds the resulting p-values to the plot with an annotation bar.
    Visualizing group differences are frequently performed by boxplots, bar plots, etc.
    Statistical test results are often needed to be annotated on these plots. 
    This package provides a convenient function that works on 'ggplot2' objects, 
    performs the desired statistical test between groups of interest and annotates the test results on the plot.
	"""
	
	homepage = "https://github.com/s6juncheng/ggpval"
	cran = "ggpval" 

	version("0.2.5", md5="1fa9002c5a21e5a990d27a7d584538aa")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
