# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcma(RPackage):
	"""R-to-Java Interface for 'CMA-ES'

	Tool for providing access to the Java version 'CMAEvolutionStrategy' of
    Nikolaus Hansen. 'CMA-ES' is the Covariance Matrix Adaptation Evolution Strategy,
    see <https://www.lri.fr/~hansen/cmaes_inmatlab.html#java>.
	"""
	
	cran = "rCMA" 

	version("1.1.1", md5="bedf6fbc7f3733e779518cc4aae6859f")

	depends_on("r@2.14:", type=("build", "run"))
