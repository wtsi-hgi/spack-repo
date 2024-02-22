# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimdistr(RPackage):
	"""Assessment of Data Trial Distributions According to the
Carlisle-Stouffer Method

	Assessment of the distributions of baseline continuous and categorical 
    variables in randomised trials. This method is based on the Carlisle-Stouffer 
    method with Monte Carlo simulations. It calculates p-values for each trial 
    baseline variable, as well as combined p-values for each trial - these p-values 
    measure how compatible are distributions of trials baseline variables with 
    random sampling. This package also allows for graphically plotting the 
    cumulative frequencies of computed p-values.
    Please note that code was partly adapted from Carlisle JB, Loadsman JA. 
    (2017) <doi:10.1111/anae.13650>.
	"""
	
	cran = "simdistr" 

	version("1.0.1", md5="a5641996c068fc634c0837d0dfdd1510")

	depends_on("r@2.10:", type=("build", "run"))
