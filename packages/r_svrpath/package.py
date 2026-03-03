# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvrpath(RPackage):
	"""The SVR Path Algorithm

	Computes the entire solution paths for Support Vector Regression(SVR) with respect to the regularization parameter, lambda and epsilon in epsilon-intensive loss function, efficiently. We call each path algorithm svrpath and epspath. See Wang, G. et al (2008) <doi:10.1109/TNN.2008.2002077> for details regarding the method.
	"""
	
	cran = "svrpath" 

	version("0.1.2", md5="2fd35f51c3ed9a3dcb6867700b22019e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-svmpath", type=("build", "run"))
