# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVlda(RPackage):
	"""Visualization of Multidimensional Longitudinal Data

	Assists in producing a plot that more effectively expresses changes over time for two different types (long format and wide format) using a consistent calling scheme for longitudinal data. It provides the ability to projection supplementary information (supplementary objects and variables) that can often occur in longitudinal data to graphs, as well as provides a new interactive implementation to perform the additional interpretation, so it is also useful for longitudinal data visuals analysis (see <http://lib.pusan.ac.kr/resource/e-article/?app=eds&mod=detail&record_id=edsker.000004649097&db_id=edsker> for more information).
	"""
	
	homepage = "https://github.com/pnuwon/vlda"
	cran = "vlda" 

	version("1.1.5", md5="776c955ba662ca12000550e603ac97a4")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggiraph", type=("build", "run"))
	depends_on("r-ggsci", type=("build", "run"))
