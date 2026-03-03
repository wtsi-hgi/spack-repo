# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParetoposstable(RPackage):
	"""Computing, Fitting and Validating the PPS Distribution

	Statistical functions to describe a Pareto Positive Stable (PPS) 
    distribution and fit it to real data. Graphical and statistical tools to 
    validate the fits are included.
	"""
	
	cran = "ParetoPosStable" 

	version("1.1", md5="cd194f0c7f07e6d07dbc99247d94c328")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-adgoftest", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
