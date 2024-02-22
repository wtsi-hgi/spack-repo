# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIncr(RPackage):
	"""Analysis of Incubation Data

	Suite of functions to study animal incubation.
    At the core of incR 
    lies an algorithm that allows for the scoring of 
    incubation behaviour. Additionally, several functions 
    extract biologically relevant metrics of incubation such as off-bout number 
    and off-bout duration - for a review of avian incubation studies, 
    see Nests, Eggs, and Incubation: New ideas about avian reproduction (2015) 
    edited by D. Charles Deeming and S. James Reynolds <doi:10.1093/acprof:oso/9780198718666.001.0001>.
	"""
	
	cran = "incR" 

	version("2.1.0", md5="8caca48de60fc7c33e9a7afea9168f8f")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-suncalc", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
