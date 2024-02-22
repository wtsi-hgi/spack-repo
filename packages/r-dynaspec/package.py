# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynaspec(RPackage):
	"""Dynamic Spectrogram Visualizations

	A set of tools to generate dynamic spectrogram visualizations in video format.
	"""
	
	homepage = "https://github.com/maRce10/dynaSpec"
	cran = "dynaSpec" 

	version("1.0.1", md5="9934b0651d6ed855760b2b44481f34a8")

	depends_on("r@3.2.1:", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-seewave", type=("build", "run"))
	depends_on("r-tuner", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-naturesounds", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-av", type=("build", "run"))
	depends_on("r-ari", type=("build", "run"))
	depends_on("r-gganimate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("ffmpeg", type=("build", "link", "run"))
