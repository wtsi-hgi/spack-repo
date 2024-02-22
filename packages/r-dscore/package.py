# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDscore(RPackage):
	"""D-Score for Child Development

	The D-score is a quantitative measure of child development. 
    The D-score follows the Rasch model. See Jacobusse, van Buuren and 
    Verkerk (2006) <doi:10.1002/sim.2351>. The user can convert 
    milestone scores from many assessment instruments into the D-score 
    and the DAZ (D-score adjusted for age). Several tools assist in 
    mapping milestone names into the 9-position Global Scale of Early 
    Development (GSED) convention. Supports calculation of the D-score 
    using 'dutch' <doi:10.1177/0962280212473300>, 
    'gcdg' <doi:10.1136/bmjgh-2019-001724> and 'gsed' conversion keys.
    The user can calculate DAZ using 'phase1' (default), 'gcdg' and 'dutch' 
    age-conditional references.
	"""
	
	homepage = "https://github.com/d-score/dscore"
	cran = "dscore" 

	version("1.8.0", md5="6032b20cf6dc558a6d35f81bacfd5376")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tidyr@1:", type=("build", "run"))
	depends_on("r-tidyselect@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
