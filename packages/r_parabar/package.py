# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParabar(RPackage):
	"""Progress Bar for Parallel Tasks

	A simple interface in the form of R6 classes for executing tasks in
    parallel, tracking their progress, and displaying accurate progress bars.
	"""
	
	homepage = "https://parabar.mihaiconstantin.com"
	cran = "parabar" 

	version("1.1.1", md5="cc0440418ee50b002869ce5ff684e789")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-callr", type=("build", "run"))
	depends_on("r-filelock", type=("build", "run"))
