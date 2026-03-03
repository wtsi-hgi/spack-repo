# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHassediagram(RPackage):
	"""Drawing Hasse Diagram

	Drawing Hasse diagram - visualization of transitive reduction of a finite partially ordered set.
	"""
	
	homepage = "https://github.com/kciomek/hasseDiagram"
	cran = "hasseDiagram" 

	version("0.2.0", md5="714a1633e0cb7d48b0644861d51a7988")

	depends_on("r-rgraphviz@2.6:", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
