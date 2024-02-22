# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiobjmatch(RPackage):
	"""Multi-Objective Matching Algorithm

	Matching algorithm based on network-flow structure. 
  Users are able to modify the emphasis on three different 
  optimization goals: two different distance measures and 
  the number of treated units left unmatched. The method is proposed by Pimentel
  and Kelz (2019) <doi:10.1080/01621459.2020.1720693>.
  The 'rrelaxiv' package, which provides an alternative solver for
	the underlying network flow problems, carries an
	academic license and is not available on CRAN, but
	may be downloaded from Github at 
	<https://github.com/josherrickson/rrelaxiv/>.
	"""
	
	cran = "MultiObjMatch" 

	version("0.1.3", md5="00ecc3e490e298f628ce7eb728a0e757")

	depends_on("r-cobalt", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-optmatch", type=("build", "run"))
	depends_on("r-matchmulti", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-rcbalance", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rlemon", type=("build", "run"))
