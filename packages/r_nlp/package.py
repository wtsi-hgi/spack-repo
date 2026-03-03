# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNlp(RPackage):
	"""Natural Language Processing Infrastructure

	Basic classes and methods for Natural Language Processing.
	"""
	
	cran = "NLP" 

	version("0.2-1", md5="91387f382da64f6e93b6c85ee6b06aa1")

	depends_on("r@3.2:", type=("build", "run"))
