# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPbcc(RPackage):
	"""Percentile-Based Control Chart

	Design and implementation of Percentile-based Shewhart Control Charts for continuous data. Faraz (2019) <doi:10.1002/qre.2384>.
	"""
	
	homepage = "https://github.com/kzst/pbcc"
	cran = "pbcc" 

	version("0.0.4", md5="34b80d6b6be0a5183e959b099571327c")

	depends_on("r@3.10:", type=("build", "run"))
	depends_on("r-rgenoud", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-qcc", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
