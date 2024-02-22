# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMotorneuron(RPackage):
	"""Analyzing Paired Neuron Discharge Times for Time-Domain
Synchronization

	The temporal relationship between motor neurons can offer 
    explanations for neural strategies. We combined functions to reduce neuron 
    action potential discharge data and analyze it for short-term, time-domain 
    synchronization. Even more so, motoRneuron combines most available methods 
    for the determining cross correlation histogram peaks and most available 
    indices for calculating synchronization into simple functions. See 
    Nordstrom, Fuglevand, and Enoka (1992) <doi:10.1113/jphysiol.1992.sp019244> 
    for a more thorough introduction.
	"""
	
	homepage = "http://github.com/tweedell/motoRneuron"
	cran = "motoRneuron" 

	version("1.0.0", md5="d4435f6eb8ced4a658866121a6817ae6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
