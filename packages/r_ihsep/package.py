# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIhsep(RPackage):
	"""Inhomogeneous Self-Exciting Process

	Simulate an inhomogeneous self-exciting process (IHSEP), or Hawkes process, with a given (possibly time-varying) baseline intensity and an excitation function. Calculate the likelihood of an IHSEP with given baseline intensity and excitation functions for an (increasing) sequence of event times. Calculate the point process residuals (integral transforms of the original event times). Calculate the mean intensity process.
	"""
	
	cran = "IHSEP" 

	version("0.3.1", md5="b0c500e62cc9fb94992ad09778c3ccc2")

	depends_on("r-lpint", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
