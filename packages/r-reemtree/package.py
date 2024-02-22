# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReemtree(RPackage):
	"""Regression Trees with Random Effects for Longitudinal (Panel)
Data

	A data mining approach for longitudinal and clustered data, 
        which combines the structure of mixed effects model with tree-based 
        estimation methods. See Sela, R.J. and Simonoff, J.S. (2012) RE-EM 
        trees: a data mining approach for longitudinal and clustered data 
        <doi:10.1007/s10994-011-5258-3>.
	"""
	
	homepage = "http://pages.stern.nyu.edu/~jsimonof/REEMtree/"
	cran = "REEMtree" 

	version("0.90.5", md5="b532f1c12fa47e715a3b7a48f8f0e981")

	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
