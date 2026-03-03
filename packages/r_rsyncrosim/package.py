# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsyncrosim(RPackage):
	"""The R Interface to 'SyncroSim'

	'SyncroSim' is a generalized framework for managing scenario-based 
    datasets (<https://syncrosim.com/>). 'rsyncrosim' provides an interface to 
    'SyncroSim'. Simulation models can be added to 'SyncroSim' in order to 
    transform these datasets, taking advantage of general features such as 
    defining scenarios of model inputs, running Monte Carlo simulations, and 
    summarizing model outputs. 'rsyncrosim' requires 'SyncroSim' 2.3.5 or higher 
    (API documentation: <https://docs.syncrosim.com/>).
	"""
	
	homepage = "<https://syncrosim.github.io/rsyncrosim/>"
	cran = "rsyncrosim" 

	version("1.5.0", md5="74ce9054e96ae473ee22638651f0ff73")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
