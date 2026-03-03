# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCffdrs(RPackage):
	"""Canadian Forest Fire Danger Rating System

	This project provides a group of new functions to calculate
    the outputs of the two main components of the Canadian Forest Fire
    Danger Rating System (CFFDRS) Van Wagner and Pickett (1985)
    <https://cfs.nrcan.gc.ca/publications?id=19973>) at various time
    scales: the Fire Weather Index (FWI) System Wan Wagner (1985)
    <https://cfs.nrcan.gc.ca/publications?id=19927> and the Fire Behaviour
    Prediction (FBP) System Forestry Canada Fire Danger Group (1992)
    <https://cfs.nrcan.gc.ca/pubwarehouse/pdfs/10068.pdf>. Some functions
    have two versions, table and raster based.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/cffdrs/"
	cran = "cffdrs" 

	version("1.9.0", md5="bc873e60ebef1083b5af79ba2928c444")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
