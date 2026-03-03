# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamtool(RPackage):
	"""Stock Assessment Methods Toolkit

	Simulation tools for closed-loop simulation are provided for the 'MSEtool' operating model to inform data-rich fisheries. 
  'SAMtool' provides a conditioning model, assessment models of varying complexity with standardized reporting, 
  model-based management procedures, and diagnostic tools for evaluating assessments inside closed-loop simulation.
	"""
	
	homepage = "https://openmse.com"
	cran = "SAMtool" 

	version("1.6.4", md5="17d7bf7eb65f5cb4383e2a80f5a11979")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-msetool@3:", type=("build", "run"))
	depends_on("r-tmb", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
	depends_on("r-vars", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
