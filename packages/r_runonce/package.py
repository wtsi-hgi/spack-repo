# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRunonce(RPackage):
	"""Run Once and Save Result

	Package 'runonce' helps automating the saving of long-running code
    to help running the same code multiple times. If you run some long-running 
    code once, it saves the result in a file on disk. Then, if the result 
    already exists, i.e. if the code has already been run and its output has 
    already been saved, it just reads the result from the stored file instead 
    of running the code again. 
	"""
	
	homepage = "https://github.com/privefl/runonce"
	cran = "runonce" 

	version("0.2.3", md5="d526997b71ff9185b5218cf3a982f0ea")

	depends_on("r-bigassertr", type=("build", "run"))
	depends_on("r-urltools", type=("build", "run"))
