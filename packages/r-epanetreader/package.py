# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpanetreader(RPackage):
	"""Read Epanet Files into R

	Reads water network simulation data in 'Epanet' text-based
    '.inp' and '.rpt' formats into R. Also reads results from 'Epanet-msx'.
    Provides basic summary information and plots.  The README file has a 
    quick introduction. See <http://www2.epa.gov/water-research/epanet> 
    for more information on the Epanet software for modeling
    hydraulic and water quality behavior of water piping systems.
	"""
	
	homepage = "https://github.com/bradleyjeck/epanetReader"
	cran = "epanetReader" 

	version("0.7.3", md5="d9c47b873812cc73d951cbb76622b979")

	depends_on("r@3:", type=("build", "run"))
