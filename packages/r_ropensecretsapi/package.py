# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRopensecretsapi(RPackage):
	"""R Package for the OpenSecrets.org API

	An R package for the OpenSecrets.org web services API.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "ropensecretsapi" 

	version("1.0.1", md5="fff4abdd6e49e48866902c9565296562")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
