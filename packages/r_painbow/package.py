# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPainbow(RPackage):
	"""Use XKCD's "Painbow" Colormap in ggplot2

	XKCD described a supposedly "bad" colormap that it called a "Painbow" (see <https://xkcd.com/2537/>). But simple tests demonstrate that under some circumstances, the colormap can perform very well, and people can find information that is difficult to detect with the ggplot2 default and even supposedly "good" colormaps like viridis. This library let's you use the Painbow in your own ggplot graphs.
	"""
	
	homepage = "https://github.com/steveharoz/painbow"
	cran = "painbow" 

	version("1.0.1", md5="4b525f6da2540178b5696a3c79f9dc7d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
