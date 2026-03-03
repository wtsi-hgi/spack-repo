# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMop(RPackage):
	"""Mobility Oriented-Parity Metric

	A set of tools to perform multiple versions of the Mobility
    Oriented-Parity metric. This multivariate analysis helps to characterize 
    levels of dissimilarity between a set of conditions of reference and another
    set of conditions of interest. If predictive models are transferred to 
    conditions different from those over which models were calibrated (trained),
    this metric helps to identify transfer conditions that differ 
    substantially from those of calibration. These tools are implemented 
    following principles proposed in Owens et al. (2013) 
    <doi:10.1016/j.ecolmodel.2013.04.011>, and expanded to obtain more detailed 
    results that aid in interpretation.
	"""
	
	homepage = "https://github.com/marlonecobos/mop"
	cran = "mop" 

	version("0.1.2", md5="717f5ab92c4e3e21103303520b2d1f2d")
	version("0.1.1", md5="f5988bfebb460ab45fccedca14d3b916")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dosnow@1:", type=("build", "run"))
	depends_on("r-foreach@1.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-snow@0.4:", type=("build", "run"))
	depends_on("r-terra@1.6.7:", type=("build", "run"))
