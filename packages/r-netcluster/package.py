# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetcluster(RPackage):
	"""Clustering for networks

	Facilitates network clustering and evaluation of cluster
        configurations.
	"""
	
	cran = "NetCluster" 

	version("0.2", md5="ba8fbf355d3ac6c6429dd650b20b3281")

	depends_on("r-sna", type=("build", "run"))
