# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDssd(RPackage):
	"""Distance Sampling Survey Design

	Creates survey designs for distance sampling surveys. These
    designs can be assessed for various effort and coverage statistics.
    Once the user is satisfied with the design characteristics they can 
    generate a set of transects to use in their distance sampling survey.
    Many of the designs implemented in this R package were first made 
    available in our 'Distance' for Windows software and are detailed in 
    Chapter 7 of Advanced Distance Sampling, Buckland et. al. (2008, 
    ISBN-13: 978-0199225873). Find out more about estimating animal/plant 
    abundance with distance sampling at <http://distancesampling.org/>. 
	"""
	
	cran = "dssd" 

	version("1.0.2", md5="157ae3cddb719a0fa3c70229644de772")

	depends_on("r-sf", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
