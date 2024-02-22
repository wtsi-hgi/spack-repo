# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreearmedtrials(RPackage):
	"""Design and Analysis of Clinical Non-Inferiority or Superiority
Trials with Active and Placebo Control

	Design and analyze three-arm non-inferiority or superiority trials
    which follow a gold-standard design, i.e. trials with an experimental treatment,
    an active, and a placebo control. Method for the following distributions are implemented:
    Poisson (Mielke and Munk (2009) <arXiv:0912.4169>), negative binomial (Muetze et al. (2016) <doi:10.1002/sim.6738>),
    normal (Pigeot et al. (2003) <doi:10.1002/sim.1450>; Hasler et al. (2009) <doi:10.1002/sim.3052>), 
    binary (Friede and Kieser (2007) <doi:10.1002/sim.2543>), nonparametric (Muetze et al. (2017) <doi:10.1002/sim.7176>),
    exponential (Mielke and Munk (2009) <arXiv:0912.4169>).
	"""
	
	homepage = "https://github.com/tobiasmuetze/ThreeArmedTrials"
	cran = "ThreeArmedTrials" 

	version("1.0-4", md5="c1047abcc35415b664514d490f84f7d2")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
