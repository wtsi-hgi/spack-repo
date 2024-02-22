# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelectiongain(RPackage):
	"""A Tool for Calculation and Optimization of the Expected Gain
from Multi-Stage Selection

	Multi-stage selection is practiced in numerous fields of life
    and social sciences and particularly in breeding. A special characteristic of
    multi-stage selection is that candidates are evaluated in successive stages
    with increasing intensity and effort, and only a fraction of the superior
    candidates is selected and promoted to the next stage. For the optimum design
    of such selection programs, the selection gain plays a crucial role. It can be
    calculated by integration of a truncated multivariate normal (MVN) distribution.
    While mathematical formulas for calculating the selection gain and the variance
    among selected candidates were developed long time ago, solutions for numerical
    calculation were not available. This package can also be used for optimizing
    multi-stage selection programs for a given total budget and different costs of
    evaluating the candidates in each stage.
	"""
	
	cran = "selectiongain" 

	version("2.0.710", md5="2f33c78ee5253d92ffcdaee488d3ae5e")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
