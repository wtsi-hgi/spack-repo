# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQubicdata(RPackage):
	"""Data employed in the vignette of the QUBIC package

	The data employed in the vignette of the QUBIC package. These data belong to Many Microbe Microarrays Database and STRING v10.
	"""
	
	homepage = "http://github.com/zy26/QUBICdata"
	bioc = "QUBICdata"

	version("1.36.0", commit="6de85a4563d3398061765e09f095dc529750a547")
	version("1.30.0", commit="6da9024c40e947dbffb971966dbebbce6e6eaa6b")

	depends_on("r@3.1:", type=("build", "run"))

