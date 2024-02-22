# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRfclust(RPackage):
	"""Random Forest Cluster Analysis

	Tools to perform random forest consensus clustering of different data types. The package is designed to accept a list of matrices from different assays, typically from high-throughput molecular profiling so that class discovery may be jointly performed. For references, please see Tao Shi & Steve Horvath (2006) <doi:10.1198/106186006X94072> & Monti et al (2003) <doi:10.1023/A:1023949509487> .
	"""
	
	cran = "RFclust" 

	version("0.1.2", md5="60e73ca0f3d3c2053ea6a10b4190556f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-consensusclusterplus", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
