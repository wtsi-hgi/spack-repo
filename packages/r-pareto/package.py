# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPareto(RPackage):
	"""The Pareto, Piecewise Pareto and Generalized Pareto Distribution

	Utilities for the Pareto, piecewise Pareto and generalized Pareto distribution
    that are useful for reinsurance pricing. In particular, the package provides
    a non-trivial algorithm that can be used to match the expected losses of a 
    tower of reinsurance layers with a layer-independent collective risk model.
    The theoretical background of the matching algorithm and most other methods
    are described in Ulrich Riegel (2018) <doi:10.1007/s13385-018-0177-3>.
	"""
	
	homepage = "https://github.com/ulrichriegel/Pareto#pareto"
	cran = "Pareto" 

	version("2.4.5", md5="59bc0cb1d1b01ec83a34f2a0b1fe062d")

	depends_on("r@2.10:", type=("build", "run"))
