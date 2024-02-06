# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCowplot(RPackage):
	"""Streamlined Plot Theme and Plot Annotations for 'ggplot2'.

	Provides various features that help with creating publication-quality
	figures with 'ggplot2', such as a set of themes, functions to align plots
	and arrange them into complex compound figures, and functions that make it
	easy to annotate plots and or mix plots with images. The package was
	originally written for internal use in the Wilke lab, hence the name (Claus
	O. Wilke's plot package). It has also been used extensively in the book
	Fundamentals of Data Visualization."""

	cran = "cowplot"

	version("1.1.3", md5="fbfdde59c0b5521ace81bdf96e79f2f6")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
