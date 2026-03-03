# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFutureBatchtools(RPackage):
	"""A Future API for Parallel and Distributed Processing using
'batchtools'

	Implementation of the Future API on top of the 'batchtools' package.
    This allows you to process futures, as defined by the 'future' package,
    in parallel out of the box, not only on your local machine or ad-hoc
    cluster of machines, but also via high-performance compute ('HPC') job
    schedulers such as 'LSF', 'OpenLava', 'Slurm', 'SGE', and 'TORQUE' / 'PBS',
    e.g. 'y <- future.apply::future_lapply(files, FUN = process)'.
	"""
	
	homepage = "https://future.batchtools.futureverse.org"
	cran = "future.batchtools" 

	version("0.12.1", md5="d0adf1c8425d5ee05b001336e7799470")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-future@1.31:", type=("build", "run"))
	depends_on("r-batchtools@0.9.16:", type=("build", "run"))
