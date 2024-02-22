# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RActcd(RPackage):
	"""Asymptotic Classification Theory for Cognitive Diagnosis

	Cluster analysis for cognitive diagnosis based on the Asymptotic Classification Theory (Chiu, Douglas & Li, 2009; <doi:10.1007/s11336-009-9125-0>). Given the sample statistic of sum-scores, cluster analysis techniques can be used to classify examinees into latent classes based on their attribute patterns. In addition to the algorithms used to classify data, three labeling approaches are proposed to label clusters so that examinees' attribute profiles can be obtained.
	"""
	
	cran = "ACTCD" 

	version("1.3-0", md5="7a2c4425c94f8b373d460e16c54a2a34")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r-methodss3", type=("build", "run"))
	depends_on("r-gdina", type=("build", "run"))
