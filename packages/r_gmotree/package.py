# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGmotree(RPackage):
	"""Get and Modify 'oTree' Data

	Manage data from 'oTree' experiments.  Import 'oTree' data and
    clean them up by using functions to deal with messy data, dropouts, and
    other problematic cases. Create IDs, calculate the time, transfer
    variables between app data frames, and delete sensitive information.
    You can also check your experimental data before running the
    experiment. Information on 'oTree' is found in Chen, D. L., Schonger, M., 
    & Wickens, C. (2016) <doi: 10.1016/j.jbef.2015.12.001>.
	"""
	
	homepage = "https://zauchnerp.github.io/gmoTree/"
	cran = "gmoTree" 

	version("1.0.1", md5="32d6228a888a73163da20c14c51fc2b0")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table@1.14.8:", type=("build", "run"))
	depends_on("r-dplyr@1.1.2:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.5.2:", type=("build", "run"))
	depends_on("r-plyr@1.8.8:", type=("build", "run"))
	depends_on("r-rlang@1.1.1:", type=("build", "run"))
	depends_on("r-rlist@0.4.6.2:", type=("build", "run"))
	depends_on("r-stringr@1.5:", type=("build", "run"))
