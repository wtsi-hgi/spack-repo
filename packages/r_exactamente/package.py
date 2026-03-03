# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RExactamente(RPackage):
	"""Explore the Exact Bootstrap Method

	Researchers often use the bootstrap to understand a sample drawn
    from a population with unknown distribution. The exact bootstrap method is a
    practical tool for exploring the distribution of small sample size data. For
    a sample of size n, the exact bootstrap method generates the entire space of
    n to the power of n resamples and calculates all realizations of the selected
    statistic. The 'exactamente' package includes functions for implementing two
    bootstrap methods, the exact bootstrap and the regular bootstrap. The
    exact_bootstrap() function applies the exact bootstrap method following
    methodologies outlined in Kisielinska (2013) <doi:10.1007/s00180-012-0350-0>.
    The regular_bootstrap() function offers a more traditional bootstrap approach,
    where users can determine the number of resamples. The e_vs_r() function
    allows users to directly compare results from these bootstrap methods. To
    augment user experience, 'exactamente' includes the function exactamente_app()
    which launches an interactive 'shiny' web application. This application
    facilitates exploration and comparison of the bootstrap methods, providing
    options for modifying various parameters and visualizing results.
	"""
	
	homepage = "https://github.com/mightymetrika/exactamente"
	cran = "exactamente" 

	version("0.1.1", md5="096ed59983126c89751186bd21a29fad")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
