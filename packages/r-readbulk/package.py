# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadbulk(RPackage):
	"""Read and Combine Multiple Data Files

	Combine multiple data files from a common directory.
    The data files will be read into R and bound together, creating a
    single large data.frame. A general function is provided along with
    a specific function for data that was collected using the open-source
    experiment builder 'OpenSesame' <https://osdoc.cogsci.nl/>.
	"""
	
	homepage = "https://github.com/pascalkieslich/readbulk"
	cran = "readbulk" 

	version("1.1.4", md5="e7416891594115b5f520f58b299e10dc")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
