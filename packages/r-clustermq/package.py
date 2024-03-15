# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClustermq(RPackage):
	"""Evaluate Function Calls on HPC Schedulers (LSF, SGE, SLURM,
PBS/Torque)

	Evaluate arbitrary function calls using workers on HPC schedulers
    in single line of code. All processing is done on the network without
    accessing the file system. Remote schedulers are supported via SSH.
	"""
	
	homepage = "https://mschubert.github.io/clustermq/"
	cran = "clustermq" 

	version("0.9.4", md5="25b14dbfad3f83234e850a9669b09c7a")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-narray", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("libzmq@4.3.0:", type=("build", "link", "run"))
