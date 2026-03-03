# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptiscale(RPackage):
	"""Optimal Scaling

	Optimal scaling of a data vector, relative to a set of targets, is
    obtained through a least-squares transformation subject to appropriate measurement
    constraints. The targets are usually predicted values from a statistical
    model. If the data are nominal level, then the transformation must be
    identity-preserving. If the data are ordinal level, then the
    transformation must be monotonic. If the data are discrete, then tied data
    values must remain tied in the optimal transformation. If the data are
    continuous, then tied data values can be untied in the optimal
    transformation.
	"""
	
	cran = "optiscale" 

	version("1.2.2", md5="87546d3db07cf78105090d70720a8657")

	depends_on("r-lattice", type=("build", "run"))
