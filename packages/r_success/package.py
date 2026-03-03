# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSuccess(RPackage):
	"""Survival Control Charts Estimation Software

	Quality control charts for survival outcomes.
    Allows users to construct the Continuous Time Generalized
    Rapid Response CUSUM (CGR-CUSUM) <doi:10.1093/biostatistics/kxac041>, 
    the Biswas & Kalbfleisch (2008)  <doi:10.1002/sim.3216> CUSUM, 
    the Bernoulli CUSUM and the risk-adjusted funnel plot for survival data 
    <doi:10.1002/sim.1970>. 
    These procedures can be used to monitor survival processes for a change 
    in the failure rate.
	"""
	
	homepage = "https://github.com/d-gomon/success"
	cran = "success" 

	version("1.0.1", md5="9cf9a9fa63d97ada8ec88ffc3d70572a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
