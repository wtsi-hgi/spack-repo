# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCbctools(RPackage):
	"""Choice-Based Conjoint Experiment Design Generation and Power
Evaluation in R

	Design and evaluate choice-based conjoint survey experiments. Generate a variety of survey designs, including random designs, full factorial designs, orthogonal designs, D-optimal designs, and Bayesian D-efficient designs as well as designs with "no choice" options and "labeled" (also known as "alternative specific") designs. Conveniently inspect the design balance and overlap, and simulate choice data for a survey design either randomly or according to a multinomial or mixed logit utility model defined by user-provided prior parameters. Conduct a power analysis for a given survey design by estimating the same model on different subsets of the data to simulate different sample sizes. Full factorial and orthogonal designs are obtained using the 'DoE.base' package (Grömping, 2018) <doi:10.18637/jss.v085.i05>. D-optimal designs are obtained using the 'AlgDesign' package (Wheeler, 2022) <https://CRAN.R-project.org/package=AlgDesign>. Bayesian D-efficient designs are obtained using the 'idefix' package (Traets et al, 2020) <doi:10.18637/jss.v096.i03>. Choice simulation and model estimation in power analyses are handled using the 'logitr' package (Helveston, 2023) <doi:10.18637/jss.v105.i10>.
	"""
	
	homepage = "https://github.com/jhelvy/cbcTools"
	cran = "cbcTools" 

	version("0.5.0", md5="137e53719d3d99f01958abf0a86af679")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-algdesign", type=("build", "run"))
	depends_on("r-doe-base", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-idefix", type=("build", "run"))
	depends_on("r-logitr@1.0.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
