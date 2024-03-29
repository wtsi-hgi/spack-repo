# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REsvis(RPackage):
	"""Visualization and Estimation of Effect Sizes

	A variety of methods are provided to estimate and visualize
    distributional differences in terms of effect sizes. Particular emphasis
    is upon evaluating differences between two or more distributions across
    the entire scale, rather than at a single point (e.g., differences in
    means). For example, Probability-Probability (PP) plots display the
    difference between two or more distributions, matched by their empirical
    CDFs (see Ho and Reardon, 2012; <doi:10.3102/1076998611411918>), allowing
    for examinations of where on the scale distributional differences are
    largest or smallest. The area under the PP curve (AUC) is an effect-size
    metric, corresponding to the probability that a randomly selected
    observation from the x-axis distribution will have a higher value
    than a randomly selected observation from the y-axis distribution. 
    Binned effect size plots are also available, in which the distributions
    are split into bins (set by the user) and separate effect sizes (Cohen's
    d) are produced for each bin - again providing a means to evaluate the
    consistency (or lack thereof) of the difference between two or more 
    distributions at different points on the scale. Evaluation of empirical 
    CDFs is also provided, with  built-in arguments for providing annotations 
    to help evaluate distributional differences at specific points (e.g., 
    semi-transparent shading). All function take a consistent argument 
    structure. Calculation of specific effect sizes is also possible. The
    following effect sizes are estimable: (a) Cohen's d, (b) Hedges' g, 
    (c) percentage above a cut, (d) transformed (normalized) percentage above 
    a cut, (e)  area under the PP curve, and (f) the V statistic (see Ho, 
    2009; <doi:10.3102/1076998609332755>), which essentially transforms the 
    area under the curve to standard deviation units. By default, effect sizes 
    are calculated for all possible pairwise comparisons, but a reference 
    group (distribution) can be specified.
	"""
	
	homepage = "https://github.com/datalorax/esvis"
	cran = "esvis" 

	version("0.3.1", md5="a75aab832637b89da92221ca35829386")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
