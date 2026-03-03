# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrimmr(RPackage):
	"""Estimation, Simulation and Reliability of Drifting Markov Models

	Performs the drifting Markov models (DMM) which are 
    non-homogeneous Markov models designed for modeling the heterogeneities of
    sequences in a more flexible way than homogeneous Markov chains or even 
    hidden Markov models. In this context, we developed an R package dedicated to 
    the estimation, simulation and the exact computation of associated reliability 
    of drifting Markov models. The implemented methods are described in
    Vergne, N. (2008), <doi:10.2202/1544-6115.1326> and
    Barbu, V.S., Vergne, N. (2019) <doi:10.1007/s11009-018-9682-8> .
	"""
	
	cran = "drimmR" 

	version("1.0.1", md5="1b2d1adccd98e86fdf564f6b7a6e40de")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-seqinr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
