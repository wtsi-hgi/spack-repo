# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIols(RPackage):
	"""Iterated Ordinary Least Squares Regression

	Addresses the 'log of zero' by developing a new family of 
    estimators called iterated Ordinary Least Squares. 
    This family nests standard approaches such as log-linear and 
    Poisson regressions, offers several computational advantages, 
    and corresponds to the correct way to perform the popular 
    log(Y + 1) transformation. For more details about how to use it, 
    see the notebook at: <https://www.davidbenatia.com/>.
	"""
	
	cran = "IOLS" 

	version("0.1.4", md5="07d14f3cc1b2389f66692e327e1446e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sandwich", type=("build", "run"))
	depends_on("r-matlib", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-randomcolor", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
