# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpdisdownsampling(RPackage):
	"""Optimal Distribution Preserving Down-Sampling of Bio-Medical
Data

	An optimized method for distribution-preserving class-proportional down-sampling of bio-medical data.
	"""
	
	homepage = "https://cran.r-project.org/package=opdisDownsampling"
	cran = "opdisDownsampling" 

	version("0.8.3", md5="df72829982cfb3c6468b87d67cf5884b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-catools", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-twosamples", type=("build", "run"))
	depends_on("r-benchmarkme", type=("build", "run"))
	depends_on("r-memuse", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
