# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBatchtools(RPackage):
	"""Tools for Computation on Batch Systems

	As a successor of the packages 'BatchJobs' and 'BatchExperiments',
    this package provides a parallel implementation of the Map function for high
    performance computing systems managed by schedulers 'IBM Spectrum LSF'
    (<https://www.ibm.com/products/hpc-workload-management>),
    'OpenLava' (<https://www.openlava.org/>), 'Univa Grid Engine'/'Oracle Grid
    Engine' (<https://www.univa.com/>), 'Slurm' (<https://slurm.schedmd.com/>),
    'TORQUE/PBS'
    (<https://adaptivecomputing.com/cherry-services/torque-resource-manager/>),
    or 'Docker Swarm' (<https://docs.docker.com/engine/swarm/>).
    A multicore and socket mode allow the parallelization on a local machines,
    and multiple machines can be hooked up via SSH to create a makeshift
    cluster. Moreover, the package provides an abstraction mechanism to define
    large-scale computer experiments in a well-organized and reproducible way.
	"""
	
	homepage = "https://github.com/mllg/batchtools"
	cran = "batchtools" 

	version("0.9.17", md5="e22ea1211f41c1c0c28175c1a151298f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-backports@1.1.2:", type=("build", "run"))
	depends_on("r-base64url@1.1:", type=("build", "run"))
	depends_on("r-brew", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-data-table@1.11.2:", type=("build", "run"))
	depends_on("r-digest@0.6.9:", type=("build", "run"))
	depends_on("r-fs@1.2:", type=("build", "run"))
	depends_on("r-progress@1.1.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-withr@2:", type=("build", "run"))
