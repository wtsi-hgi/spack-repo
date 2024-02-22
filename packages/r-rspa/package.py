# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRspa(RPackage):
	"""Adapt Numerical Records to Fit (in)Equality Restrictions

	Minimally adjust the values of numerical records in a data.frame, such
    that each record satisfies a predefined set of equality and/or inequality
    constraints. The constraints can be defined using the 'validate' package. 
    The core algorithms have recently been moved to the 'lintools' package,
    refer to 'lintools' for a more basic interface and access to a version
    of the algorithm that works with sparse matrices.
	"""
	
	homepage = "https://github.com/markvanderloo/rspa"
	cran = "rspa" 

	version("0.2.8", md5="8af718284fdd0de31dd07e61730d7862")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-validate", type=("build", "run"))
	depends_on("r-lintools", type=("build", "run"))
