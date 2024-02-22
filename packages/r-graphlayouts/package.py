# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphlayouts(RPackage):
	"""Additional Layout Algorithms for Network Visualizations.

	Several new layout algorithms to visualize networks are provided which are
	not part of 'igraph'. Most are based on the concept of stress majorization
	by Gansner et al. (2004) <doi:10.1007/978-3-540-31843-9_25>. Some more
	specific algorithms allow to emphasize hidden group structures in networks
	or focus on specific nodes."""

	cran = "graphlayouts"

	version("1.1.0", md5="7b16bec55face494bbd0ea00503acc86")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
