# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWorkloopr(RPackage):
	"""Analysis of Work Loops and Other Data from Muscle Physiology
Experiments

	Functions for the import, transformation, and analysis of data 
    from muscle physiology experiments. The work loop technique is used to 
    evaluate the mechanical work and power output of muscle. Josephson (1985) 
    <doi:10.1242/jeb.114.1.493> modernized the technique for
    application in comparative biomechanics. Although our initial motivation 
    was to provide functions to analyze work loop experiment data, as we 
    developed the package we incorporated the ability to analyze data from 
    experiments that are often complementary to work loops. There are currently 
    three supported experiment types: work loops, simple twitches, and tetanus 
    trials. Data can be imported directly from .ddf files or via an object 
    constructor function. Through either method, data can then be cleaned or 
    transformed via methods typically used in studies of muscle physiology. 
    Data can then be analyzed to determine the timing and magnitude of force 
    development and relaxation (for isometric trials) or the magnitude of work, 
    net power, and instantaneous power among other things (for work loops). 
    Although we do not provide plotting functions, all resultant objects are 
    designed to be friendly to visualization via either base-R plotting or 
    'tidyverse' functions.
 This package has been peer-reviewed by rOpenSci (v. 1.1.0).
	"""
	
	homepage = "https://docs.ropensci.org/workloopR/"
	cran = "workloopR" 

	version("1.1.4", md5="46867a50617a21b87cc9e67649839848")

	depends_on("r-pracma@2.0.7:", type=("build", "run"))
	depends_on("r-signal@0.7.6:", type=("build", "run"))
