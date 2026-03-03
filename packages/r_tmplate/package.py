# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmplate(RPackage):
	"""Code Generation Based on Templates

	Define general templates with tags that can be replaced by content depending on arguments and objects to modify the final output of the document.
	"""
	
	homepage = "<https://marioma.me?i=soft>"
	cran = "tmplate" 

	version("0.0.3", md5="e2d5159a459689755951a84088ca92ab")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-trnslate", type=("build", "run"))
