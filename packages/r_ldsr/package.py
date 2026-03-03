# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLdsr(RPackage):
	"""Linear Dynamical System Reconstruction

	Streamflow (and climate) reconstruction using Linear Dynamical Systems. 
    The advantage of this method is the additional state trajectory which can reveal more information 
    about the catchment or climate system. For details of the method please refer to Nguyen and Galelli 
    (2018) <doi:10.1002/2017WR022114>.
	"""
	
	homepage = "https://github.com/ntthung/ldsr"
	cran = "ldsr" 

	version("0.0.2", md5="3f22df77589f50f8c14dc62b87465c03")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
