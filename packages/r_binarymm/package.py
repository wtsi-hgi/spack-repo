# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBinarymm(RPackage):
	"""Flexible Marginalized Models for Binary Correlated Outcomes

	Estimates marginalized mean and dependence model parameters for correlated binary response data. 
             Dependence model may include transition and/or latent variable terms. 
             Methods are described in: Schildcrout and Heagerty (2007) <doi:10.1111/j.1541-0420.2006.00680.x>, Heagerty (1999) <doi:10.1111/j.0006-341x.1999.00688.x>, Heagerty (2002) <doi:10.1111/j.0006-341x.2002.00342.x>.
	"""
	
	cran = "binaryMM" 

	version("0.1.1", md5="3ba30fdc32e3d4e4c3b4e12a18426d8b")

	depends_on("r-fastghquad", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
