# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKsharp(RPackage):
	"""Cluster Sharpening

	Clustering typically assigns data points into discrete groups, but the clusters can sometimes be indistinct. Cluster sharpening adjusts an existing clustering to create contrast between groups. This package provides a general interface for cluster sharpening along with several implementations based on different excision criteria.
	"""
	
	homepage = "https://github.com/tkonopka/ksharp"
	cran = "ksharp" 

	version("0.1.0.1", md5="6f06f60b33ddf0f208c3d7e721c66288")

	depends_on("r@3.5:", type=("build", "run"))
