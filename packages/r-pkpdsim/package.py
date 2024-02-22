# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPkpdsim(RPackage):
	"""Tools for Performing Pharmacokinetic-Pharmacodynamic Simulations

	Simulate dose regimens for pharmacokinetic-pharmacodynamic (PK-PD)
        models described by differential equation (DE) systems. Simulation using 
        ADVAN-style analytical equations is also supported (Abuhelwa et al. (2015) 
        <doi:10.1016/j.vascn.2015.03.004>).
	"""
	
	homepage = "https://github.com/InsightRX/PKPDsim"
	cran = "PKPDsim" 

	version("1.3.0", md5="ef1a6eac27cc447872d9e817f65cd544")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp@0.12.9:", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
