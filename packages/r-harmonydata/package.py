# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHarmonydata(RPackage):
	"""R Library for 'Harmony'

	'Harmony' is a tool using AI which allows you to compare items from questionnaires and identify similar content. You can try 'Harmony' at <https://harmonydata.ac.uk/app/> and you can read our blog at <https://harmonydata.ac.uk/blog/> or at <https://fastdatascience.com/how-does-harmony-work/>. Documentation at <https://harmonydata.ac.uk/harmony-r-released/>.
	"""
	
	homepage = "<https://harmonydata.ac.uk>"
	cran = "harmonydata" 

	version("0.1.1", md5="fa7218a81ae1264ac9fdbc6bd6d0069a")

	depends_on("r-httr", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
