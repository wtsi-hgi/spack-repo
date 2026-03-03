# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTailclassifier(RPackage):
	"""Tail Classifier

	The function TailClassifier() suggests one of the following types of tail for your discrete data: 1) Power decaying tail; 2) Sub-exponential decaying tail; and 3) Near-exponential decaying tail. The function also provides an estimate of the parameter for the classified-distribution as a reference.
	"""
	
	cran = "TailClassifier" 

	version("0.1.1", md5="b829e6916de4e6b4614dee8d9a4de482")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
