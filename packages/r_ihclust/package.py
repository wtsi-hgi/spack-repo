# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIhclust(RPackage):
	"""Iterative Hierarchical Clustering (IHC)

	Provides a set of tools to
  i) identify geographic areas with significant change over time in drug utilization, and 
  ii) characterize common change over time patterns among the time series for multiple geographic areas.
  For reference, see below:
    1. Song, J., Carey, M., Zhu, H., Miao, H., Ram´ırez, J. C., & Wu, H. (2018) <doi:10.1504/IJCBDD.2018.10011910>
    2. Wu, S., Wu, H. (2013) <doi:10.1186/1471-2105-14-6>
    3. Carey, M., Wu, S., Gan, G. & Wu, H. (2016) <doi:10.1016/j.idm.2016.07.001>.
	"""
	
	cran = "ihclust" 

	version("0.1.0", md5="93c73e52dabd8fc87bf185173ce93ea8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-factoextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
