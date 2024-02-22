# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElasdics(RPackage):
	"""Elastic Analysis of Sparse, Dense and Irregular Curves

	Provides functions to align curves and to compute mean curves based on the 
    elastic distance defined in the square-root-velocity framework. For more details on 
    this framework see Srivastava and Klassen (2016, <doi:10.1007/978-1-4939-4020-2>). 
    For more theoretical details on our methods and algorithms see 
    Steyer et al. (2023, <doi:10.1111/biom.13706>) and Steyer et al. (2023, <arXiv:2305.02075>).
	"""
	
	cran = "elasdics" 

	version("1.1.3", md5="4405b3a3405612e6e18a029dddfc2fc8")

	depends_on("r-numderiv", type=("build", "run"))
