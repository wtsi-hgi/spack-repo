# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorbi(RPackage):
	"""Collection of Rudimentary Bioinformatics Tools

	Provides a bundle of basic and fundamental bioinformatics tools,
    such as network querying and alignment, subnetwork extraction and search,
    network biomarker identification.
	"""
	
	homepage = "https://github.com/wulingyun/Corbi"
	cran = "Corbi" 

	version("0.6-2", md5="03a8288320dd9dac67cea18d62d9e5af")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-crf", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
