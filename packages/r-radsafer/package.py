# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadsafer(RPackage):
	"""Radiation Safety

	Provides functions for radiation safety, also known as
    "radiation protection" and "radiological control". The science of 
    radiation protection is called "health physics" and its engineering 
    functions are called "radiological engineering". Functions in this 
    package cover many of the computations needed by radiation safety 
    professionals. Examples include: obtaining updated calibration and
    source check values for radiation monitors to account for radioactive 
    decay in a reference source, simulating instrument readings to better
    understand measurement uncertainty, correcting instrument readings 
    for geometry and ambient atmospheric conditions. Many of these 
    functions are described in Johnson and Kirby (2011, ISBN-13:  
    978-1609134198). Utilities are also included for developing inputs 
    and processing outputs with radiation transport codes, such as MCNP, 
    a general-purpose Monte Carlo N-Particle code that can be used for 
    neutron, photon, electron, or coupled neutron/photon/electron transport
    (Werner et. al. (2018) <doi:10.2172/1419730>).
	"""
	
	homepage = "https://github.com/markhogue/radsafer"
	cran = "radsafer" 

	version("2.3.0", md5="7ed4c720a2d78913634263101ab598a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-raddata", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scatterplot3d", type=("build", "run"))
	depends_on("r-ggthemes", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
