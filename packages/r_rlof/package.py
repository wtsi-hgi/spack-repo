# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlof(RPackage):
	"""R Parallel Implementation of Local Outlier Factor(LOF)

	R parallel implementation of Local Outlier Factor(LOF) which uses multiple CPUs to significantly speed up the LOF computation for large datasets. (Note: The overall performance depends on the computers especially the number of the cores).It also supports multiple k values to be calculated in parallel, as well as various distance measures in addition to the default Euclidean distance. 
	"""
	
	cran = "Rlof" 

	version("1.1.3", md5="cec16ae7598f6c0b7356bedb6ae67b6a")

	depends_on("r@2.14:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
