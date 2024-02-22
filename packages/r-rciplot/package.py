# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRciplot(RPackage):
	"""Plot Jacobson-Truax Reliable Change Indices

	The concept of reliable and clinically significant change
    (Jacobson & Truax, 1991) helps you answer the following questions for a
    sample with two measurements at different points in time (pre & post):
    Which proportion of my sample has a (considering the reliability of the
    instrument) probably not-just-by-chance difference in pre- vs. post-scores?
    Which proportion of my sample does not only change in a statistically
    significant way (see question one), but also in a clinically significant way
    (e.g. change from a test score regarded "dysfunctional" to a score regarded
    "functional")?
    This package allows you to very easily create a scatterplot of your sample
    in which the x-axis maps to the pre-scores, the y-axis maps to the
    post-scores and several graphical elements (lines, colors) allow you to gain
    a quick overview about reliable changes in these scores.
    An example of this kind of plot is Figure 2 of Jacobson & Truax (1991).
    Referenced article:
    Jacobson, N. S., & Truax, P. (1991) <doi:10.1037/0022-006X.59.1.12>.
	"""
	
	homepage = "https://gitlab.com/REDS1736/rciplot"
	cran = "rciplot" 

	version("0.1.1", md5="923b99fca3de8a38e99a878cf5dbf61e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
