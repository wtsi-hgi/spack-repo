# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGggap(RPackage):
	"""Streamlined Creation of Segments on the Y-Axis of 'ggplot2'
Plots

	The function gggap() streamlines the creation of segments on
    the y-axis of 'ggplot2' plots which is otherwise not a trivial task to
    accomplish.
	"""
	
	homepage = "https://github.com/cmoralesmx/gggap"
	cran = "gggap" 

	version("1.0.1", md5="a0e67bfa566ce38a1b3afe712351c0dd")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
