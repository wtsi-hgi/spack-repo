# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDemic(RPackage):
	"""Dynamic Estimator of Microbial Communities

	Multi-sample algorithm based on contigs and coverage values, to 
    infer the relative distances of contigs from the replication origin and to 
    accurately compare bacterial growth rates between samples. Yuan Gao and 
    Hongzhe Li (2018) <doi:10.1038/s41592-018-0182-0>.
	"""
	
	homepage = "https://github.com/Ulthran/DEMIC"
	cran = "demic" 

	version("2.0.0", md5="7fbd496f2a930c6bda35a9a5ddd17c53")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix@1.6.2:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
