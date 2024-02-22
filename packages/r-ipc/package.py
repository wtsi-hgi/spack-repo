# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpc(RPackage):
	"""Tools for Message Passing Between Processes

	Provides tools for passing messages between R processes. 
    Shiny examples are provided showing how to perform useful tasks such as: 
    updating reactive values from within a future, progress bars for long running 
    async tasks, and interrupting async tasks based on user input.
	"""
	
	homepage = "https://github.com/fellstat/ipc"
	cran = "ipc" 

	version("0.1.4", md5="9a9c81a0defed2bded079dfe51b1ae24")

	depends_on("r-r6", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-txtq", type=("build", "run"))
