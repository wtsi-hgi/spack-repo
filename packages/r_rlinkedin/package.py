# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlinkedin(RPackage):
	"""Access to the LinkedIn API via R

	A series of functions that allow users
    to access the 'LinkedIn' API to get information about connections,
    search for people and jobs, share updates with their network,
    and create group discussions.  For more information about using
    the API please visit <https://developer.linkedin.com/>.
	"""
	
	homepage = "https://github.com/mpiccirilli/Rlinkedin"
	cran = "Rlinkedin" 

	version("0.2", md5="7bc738045a7e3dea0f8aa0dbcd33a506")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-httpuv", type=("build", "run"))
