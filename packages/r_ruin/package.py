# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRuin(RPackage):
	"""Simulation of Various Risk Processes

	A (not yet exhaustive) collection of common models of risk
    processes in actuarial science, represented as formal S4 classes. Each class
    (risk model) has a simulator of its path, and a plotting function. Further, 
    a Monte-Carlo estimator of a ruin probability for a finite time is
    implemented, using a parallel computation. Currently, the package extends
    two classical risk models Cramer-Lundberg and Sparre Andersen models by
    including capital injections, that are positive jumps (see Breuer L. and
    Badescu A.L. (2014) <doi:10.1080/03461238.2011.636969>). The intent of the
    package is to provide a user-friendly interface for ruin processes'
    simulators, as well as a solid and extensible structure for future
    extensions.
	"""
	
	homepage = "http://github.com/irudnyts/ruin"
	cran = "ruin" 

	version("0.1.1", md5="9c0ad44961c15eba33346d667ffe4b2f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@2.2.1:", type=("build", "run"))
