# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPvplr(RPackage):
	"""Performance Loss Rate Analysis Pipeline

	The pipeline contained in this package provides tools used in the
    Solar Durability and Lifetime Extension Center (SDLE) for the analysis of
    Performance Loss Rates (PLR) in real world photovoltaic systems. Functions
    included allow for data cleaning, feature correction, power predictive modeling, 
    PLR determination, and uncertainty bootstrapping through various methods 
    <doi:10.1109/PVSC40753.2019.8980928>.
    The vignette "Pipeline Walkthrough" gives
    an explicit run through of typical package usage. 
    This material is based upon work supported by the U.S Department
    of Energy's Office of Energy Efficiency and Renewable Energy (EERE) under
    Solar Energy Technologies Office (SETO) Agreement Number DE-EE-0008172. 
    This work made use of the High Performance Computing Resource in the 
    Core Facility for Advanced Research Computing at
    Case Western Reserve University. 
	"""
	
	cran = "PVplr" 

	version("0.1.2", md5="6ac824e48429ed70c8777aa76e39e5c4")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.7.8:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-broom@0.5.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.1:", type=("build", "run"))
	depends_on("r-stlplus@0.5.1:", type=("build", "run"))
	depends_on("r-cluster@2.0.7.1:", type=("build", "run"))
	depends_on("r-purrr@0.3.3:", type=("build", "run"))
	depends_on("r-tidyr@1.1.1:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2.1:", type=("build", "run"))
	depends_on("r-rlang@0.3.1:", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
