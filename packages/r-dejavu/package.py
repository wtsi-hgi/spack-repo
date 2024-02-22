# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDejavu(RPackage):
	"""Multiple Imputation for Recurrent Events

	Performs reference based multiple imputation of recurrent event data
    based on a negative binomial regression model, as described
    by Keene et al (2014) <doi:10.1002/pst.1624>.
	"""
	
	cran = "dejaVu" 

	version("0.3.0", md5="1dc35dd5efa4093863edf497e5271422")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
