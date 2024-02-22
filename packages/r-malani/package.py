# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMalani(RPackage):
	"""Machine Learning Assisted Network Inference

	Find dark genes. These genes are often disregarded due to no detected mutation or differential expression, but are important in coordinating the functionality in cancer networks.
	"""
	
	cran = "malani" 

	version("1.0", md5="9b76c56b1877b6dd88abf337fd24d665")

	depends_on("r-e1071", type=("build", "run"))
