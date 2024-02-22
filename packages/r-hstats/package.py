# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHstats(RPackage):
	"""Interaction Statistics

	Fast, model-agnostic implementation of different H-statistics
    introduced by Jerome H. Friedman and Bogdan E. Popescu (2008)
    <doi:10.1214/07-AOAS148>.  These statistics quantify interaction
    strength per feature, feature pair, and feature triple.  The package
    supports multi-output predictions and can account for case weights.
    In addition, several variants of the original statistics are provided.
    The shape of the interactions can be explored through partial
    dependence plots or individual conditional expectation plots. 'DALEX'
    explainers, meta learners ('mlr3', 'tidymodels', 'caret') and most
    other models work out-of-the-box.
	"""
	
	homepage = "https://github.com/mayer79/hstats"
	cran = "hstats" 

	version("1.1.2", md5="ec7134f6d408db686da18cba480d7b2c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
