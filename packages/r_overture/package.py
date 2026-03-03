# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROverture(RPackage):
	"""Tools for Writing MCMC

	Simplifies MCMC setup by automatically looping through sampling 
    functions and saving the results.  Reduces the memory footprint of running 
    MCMC and saves samples to disk as the chain runs.  Allows samples from the 
    chain to be analyzed while the MCMC is still running.  Provides functions 
    for commonly performed operations such as calculating Metropolis acceptance 
    ratios and creating adaptive Metropolis samplers.  References: Roberts and 
    Rosenthal (2009) <doi:10.1198/jcgs.2009.06134>.
	"""
	
	homepage = "https://github.com/kurtis-s/overture"
	cran = "overture" 

	version("0.4-0", md5="1811dc9a07ac534be1d5e83bb6fb7256")

	depends_on("r-bigmemory", type=("build", "run"))
