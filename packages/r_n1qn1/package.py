# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RN1qn1(RPackage):
	"""Port of the 'Scilab' 'n1qn1' Module for Unconstrained BFGS
Optimization

	Provides 'Scilab' 'n1qn1'. This takes more memory than traditional L-BFGS.  The n1qn1 routine is useful since it allows prespecification of a Hessian.
       If the Hessian is near enough the truth in optimization it can speed up the optimization problem. The algorithm is described in the
       'Scilab' optimization documentation located at 
       <https://www.scilab.org/sites/default/files/optimization_in_scilab.pdf>. This version uses manually modified code from 'f2c' to make this a C only binary.
	"""
	
	homepage = "https://github.com/nlmixr2/n1qn1c"
	cran = "n1qn1" 

	version("6.0.1-11", md5="3bcf9d87c6a4eabf09d12716a5c55dcb", url="https://cran.r-project.org/src/contrib/n1qn1_6.0.1-11.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.5.600.2:", type=("build", "run"))
