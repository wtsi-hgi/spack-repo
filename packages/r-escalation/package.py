# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REscalation(RPackage):
	"""A Modular Approach to Dose-Finding Clinical Trials

	Methods for working with dose-finding clinical trials. We provide 
    implementations of many dose-finding clinical trial designs, including the 
    continual reassessment method (CRM) by O'Quigley et al. (1990) 
    <doi:10.2307/2531628>, the toxicity probability interval (TPI) design by Ji
    et al. (2007) <doi:10.1177/1740774507079442>, the modified TPI (mTPI) design
    by Ji et al. (2010) <doi:10.1177/1740774510382799>, the Bayesian optimal 
    interval design (BOIN) by Liu & Yuan (2015) <doi:10.1111/rssc.12089>, EffTox
    by Thall & Cook (2004) <doi:10.1111/j.0006-341X.2004.00218.x>; the design of
    Wages & Tait (2015) <doi:10.1080/10543406.2014.920873>, and the 3+3 
    described by Korn et al. (1994) <doi:10.1002/sim.4780131802>. All designs
    are implemented with a common interface. We also offer optional additional 
    classes to tailor the behaviour of all designs, including avoiding skipping 
    doses, stopping after n patients have been treated at the recommended dose,  
    stopping when a toxicity condition is met, or demanding that n patients are 
    treated before stopping is allowed. By daisy-chaining together these classes
    using the pipe operator from 'magrittr', it is simple to tailor the 
    behaviour of a dose-finding design so it behaves how the trialist wants.
    Having provided a flexible interface for specifying designs, we then provide
    functions to run simulations and calculate dose-paths for future cohorts of 
    patients.
	"""
	
	cran = "escalation" 

	version("0.1.8", md5="c24661184de7c36457a8c7f0e35bddcf")

	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-dfcrm", type=("build", "run"))
	depends_on("r-boin", type=("build", "run"))
	depends_on("r-trialr@0.1.5:", type=("build", "run"))
	depends_on("r-diagrammer", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-binom", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
