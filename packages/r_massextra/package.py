# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassextra(RPackage):
	"""Some 'MASS' Enhancements

	Some enhancements, extensions and additions
    to the facilities of the recommended 'MASS' package 
    that are useful mainly for teaching purposes, with
    more convenient default settings and user interfaces.
    Key functions from 'MASS' are imported and re-exported
    to avoid masking conflicts.  In addition we provide
    some additional functions mainly used to illustrate
    coding paradigms and techniques, such as Gramm-Schmidt
    orthogonalisation and generalised eigenvalue problems.  
	"""
	
	cran = "MASSExtra" 

	version("1.2.2", md5="c729c9d36456028b997cb5ef62a61661")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-demokde", type=("build", "run"))
