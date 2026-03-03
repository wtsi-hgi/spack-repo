# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCgrcusum(RPackage):
	"""Continuous Time Generalized Rapid Response CUSUM

	Allows users to construct the Continuous Time Generalized Rapid 
            Response CUSUM (CGR-CUSUM), Biswas & Kalbfleisch (2008) 
            <doi:10.1002/sim.3296> CUSUM, Binary CUSUM and risk-adjusted funnel 
            plot for survival data. These procedures can be used to monitor
            survival processes and detect problems in their quality.
	"""
	
	homepage = "https://github.com/d-gomon/cgrcusum"
	cran = "cgrcusum" 

	version("0.1.0", md5="acd50f700debb664c22d9b30a2483215")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
