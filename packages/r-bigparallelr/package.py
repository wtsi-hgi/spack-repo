# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RBigparallelr(RPackage):
	"""Easy Parallel Tools

	Utility functions for easy parallelism in R. Include some reexports
    from other packages, utility functions for splitting and parallelizing over
    blocks, and choosing and setting the number of cores used.
	"""
	
	homepage = "https://github.com/privefl/bigparallelr"
	cran = "bigparallelr" 

	version("0.3.2", md5="517fa3e8408d45a39e3a3dba826bd145")

	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-bigassertr@0.1.1:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-flock", type=("build", "run"))
	depends_on("r-parallelly", type=("build", "run"))
	depends_on("r-rhpcblasctl", type=("build", "run"))
