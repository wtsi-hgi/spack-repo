# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RForceplate(RPackage):
	"""Processing Force-Plate Data

	Process raw force-plate data (txt-files) by segmenting them into trials and, if needed, calculating (user-defined) descriptive 
    statistics of variables for user-defined time bins (relative to trigger onsets) for each trial. When segmenting the data a baseline 
    correction, a filter, and a data imputation can be applied if needed. Experimental data can also be processed and combined with the 
    segmented force-plate data. This procedure is suggested by Johannsen et al. (2023) <doi:10.6084/m9.figshare.22190155> and some of the 
    options (e.g., choice of low-pass filter) are also suggested by Winter (2009) <doi:10.1002/9780470549148>.
	"""
	
	homepage = "https://github.com/RaphaelHartmann/forceplate"
	cran = "forceplate" 

	version("1.1-3", md5="fa5196e2c06b05df781663df9f9be706")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
