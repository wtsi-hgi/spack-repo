# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRadous(RPackage):
	"""Query Random User Data from the Random User Generator API

	Generate random user data from the Random User Generator API.
    For more information, see <https://randomuser.me/>.
	"""
	
	homepage = "https://github.com/feddelegrand7/radous"
	cran = "radous" 

	version("0.1.3", md5="075a4e7a5911d93b4ad4cb2d41c30169")

	depends_on("r-glue", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
