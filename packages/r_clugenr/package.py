# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClugenr(RPackage):
	"""Multidimensional Cluster Generation Using Support Lines

	An implementation of the clugen algorithm for generating
    multidimensional clusters with arbitrary distributions. Each cluster is
    supported by a line segment, the position, orientation and length of which
    guide where the respective points are placed. This package is described in
    Fachada & de Andrade (2023) <doi:10.1016/j.knosys.2023.110836>.
	"""
	
	homepage = "https://clugen.github.io/clugenr/"
	cran = "clugenr" 

	version("1.0.3", md5="bdaf9eef396eeeb13b9a767dab458744")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
