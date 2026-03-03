# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScalelink(RPackage):
	"""Create Scale Linkage Scores

	Perform a 'probabilistic' linkage of two data files using a scaling procedure using the methods described in Goldstein, H., Harron, K. and Cortina-Borja, M. (2017) <doi:10.1002/sim.7287>.
	"""
	
	cran = "Scalelink" 

	version("1.0", md5="a1732bd004b03167078710be717736c8")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
