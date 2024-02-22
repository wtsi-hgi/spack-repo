# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHpcwld(RPackage):
	"""High Performance Cluster Models Based on Kiefer-Wolfowitz
Recursion

	Probabilistic models describing the behavior 
	of workload and queue on a High Performance Cluster and computing GRID 
	under FIFO service discipline basing on modified Kiefer-Wolfowitz 
	recursion. Also sample data for inter-arrival times, service times, 
	number of cores per task and waiting times of HPC of Karelian 
	Research Centre are included, measurements took place from 06/03/2009 to 02/30/2011.
	Functions provided to import/export workload traces in Standard Workload Format (swf).
	Stability condition of the model may be verified either exactly, or approximately.
	Stability analysis: see Rumyantsev and Morozov (2017) <doi:10.1007/s10479-015-1917-2>,
	workload recursion: see Rumyantsev (2014) <doi:10.1109/PDCAT.2014.36>.
	"""
	
	cran = "hpcwld" 

	version("0.6-5", md5="89e592a59ae667dfc73a84c159d8fea3")

	depends_on("r@2.10:", type=("build", "run"))
