# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbdmpi(RPackage):
	"""R Interface to MPI for HPC Clusters (Programming with Big Data
Project)

	A simplified, efficient, interface to MPI for HPC clusters. It is
        a derivation and rethinking of the Rmpi package. pbdMPI embraces the
        prevalent parallel programming style on HPC clusters. Beyond the
        interface, a collection of functions for global work with
        distributed data and resource-independent RNG reproducibility is
        included. It is based on S4 classes and methods. 
	"""
	
	homepage = "https://pbdr.org/"
	cran = "pbdMPI" 

	version("0.5-1", md5="9aee917730ba399eeccae27c080545fe")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-float", type=("build", "run"))
	depends_on("openmpi", type=("build", "link", "run"))
