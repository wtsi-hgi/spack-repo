# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpencl(RPackage):
	"""Interface allowing R to use OpenCL

	This package provides an interface to OpenCL, allowing R to leverage computing power of GPUs and other HPC accelerator devices.
	"""
	
	homepage = "http://www.rforge.net/OpenCL/"
	cran = "OpenCL" 

	version("0.2-10", md5="c7cedff20a949d3245bd602e41dfd5bb")

	depends_on("r@2:", type=("build", "run"))
	depends_on("ocl-icd+headers", type=("build", "link", "run"))
