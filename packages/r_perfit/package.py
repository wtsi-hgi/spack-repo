# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPerfit(RPackage):
	"""Person Fit

	Several person-fit statistics 
  (PFSs; Meijer and Sijtsma, 2001, <doi:10.1177/01466210122031957>) 
  are offered. These statistics allow assessing whether
  individual response patterns to tests or questionnaires are (im)plausible given 
  the other respondents in the sample or given a specified item response theory model. Some PFSs apply to 
  dichotomous data, such as the likelihood-based PFSs (lz, lz*) and the group-based PFSs 
  (personal biserial correlation, caution index, (normed) number of Guttman errors, 
  agreement/disagreement/dependability statistics, U3, ZU3, NCI, Ht). PFSs suitable to polytomous data include
  extensions of lz, U3, and (normed) number of Guttman errors. 
	"""
	
	cran = "PerFit" 

	version("1.4.6", md5="1ede41afc67dce5358d6e873b5e4d4f9")

	depends_on("r-ltm", type=("build", "run"))
	depends_on("r-mirt", type=("build", "run"))
	depends_on("r-fda", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-irtoys", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
