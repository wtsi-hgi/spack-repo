# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDyntaper(RPackage):
	"""Dynamic Stem Profile Models, AKA Tree Taper Equations

	Performs calculations with tree taper (or stem
    profile) equations, including model fitting. The package
    implements the methods from García, O. (2015) "Dynamic
    modelling of tree form"
    <http://mcfns.net/index.php/Journal/article/view/MCFNS7.1_2>.
    The models are parsimonious, describe well the tree bole shape
    over its full length, and are consistent with wood formation
    mechanisms through time.
	"""
	
	homepage = "https://github.com/ogarciav/dyntaper"
	cran = "dyntaper" 

	version("1.1", md5="27dadc9e79593127537e6fd57032615b")

	depends_on("r@2.10:", type=("build", "run"))
