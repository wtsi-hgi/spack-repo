# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrepast(RPackage):
	"""Invoke 'Repast Simphony' Simulation Models

	An R and Repast integration tool for running individual-based
    (IbM) simulation models developed using 'Repast Simphony' Agent-Based framework
    directly from R code supporting multicore execution. This package 
    integrates 'Repast Simphony' models within R environment, making easier 
    the tasks of running and analyzing model output data for 
    automated parameter calibration and for carrying out uncertainty and
    sensitivity analysis using the power of R environment.
	"""
	
	homepage = "https://github.com/antonio-pgarcia/rrepast"
	cran = "rrepast" 

	version("0.8.0", md5="d3518926284aa61f5eaca00c0eb69100")

	depends_on("r-lhs", type=("build", "run"))
	depends_on("r-sensitivity", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-rjava", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
