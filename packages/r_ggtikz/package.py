# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgtikz(RPackage):
	"""Post-Process 'ggplot2' Plots with 'TikZ' Code Using Plot
Coordinates

	Annotation of 'ggplot2' plots with arbitrary 'TikZ' code, using absolute data or relative plot coordinates.
	"""
	
	homepage = "https://github.com/osthomas/ggtikz"
	cran = "ggtikz" 

	version("0.1.2", md5="b263e7b29dffe6fea5cdad1b1c6e820c")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-tikzdevice", type=("build", "run"))
