# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCirclize(RPackage):
	"""Circular Visualization.

	Circular layout is an efficient way for the visualization of huge amounts
	of information. Here this package provides an implementation  of circular
	layout generation in R as well as an enhancement of available software. The
	flexibility of the package is based on the usage of low-level graphics
	functions such that self-defined high-level graphics can be easily
	implemented by users for specific purposes. Together with the seamless
	connection between the powerful computational and visual environment in R,
	it gives users more convenience and freedom to design figures for  better
	understanding complex patterns behind multiple dimensional data.  The
	package is described in Gu et al. 2014
	<doi:10.1093/bioinformatics/btu393>."""

	cran = "circlize"

	version("0.4.16", md5="b71bcb6a045be622a67359ce537e1ee4")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-globaloptions@0.1.2:", type=("build", "run"))
	depends_on("r-shape", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
