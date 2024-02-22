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

	version("0.9.3", md5="31e060c44e564a531e4e0305846c8c84")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-narray", type=("build", "run"))
	depends_on("r-globals", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("libzmq@4.3.0:", type=("build", "link", "run"))
