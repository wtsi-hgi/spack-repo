# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpd(RPackage):
	"""Semi Parametric Distribution

	The Semi Parametric Piecewise Distribution blends the Generalized Pareto Distribution for the tails with a kernel based interior.
	"""
	
	homepage = "http://www.unstarched.net"
	cran = "spd" 

	version("2.0-1", md5="fb9951d399bd2871e7f0d3f5bd96ef29")

	depends_on("r-kernsmooth", type=("build", "run"))
