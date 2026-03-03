# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REcho(RPackage):
	"""Echo Code Evaluations

	Capture code evaluations and script executions by expressions,
    outputs, and condition calls for logging.
	"""
	
	homepage = "https://github.com/jmbarbone/echo"
	cran = "echo" 

	version("0.1.0", md5="8554df5a360d789d9e69a0f636f47924")

	depends_on("r@3.6:", type=("build", "run"))
