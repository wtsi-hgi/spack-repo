# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRslurm(RPackage):
	"""Submit R Calculations to a 'Slurm' Cluster

	Functions that simplify submitting R scripts to a 'Slurm' 
    workload manager, in part by automating the division of embarrassingly
    parallel calculations across cluster nodes.
	"""
	
	homepage = "https://www.earthdatascience.org/rslurm/"
	cran = "rslurm" 

	version("0.6.2", md5="e4d9a59160b587558895573d0ad56319")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-whisker@0.3:", type=("build", "run"))
