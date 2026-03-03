# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrosshap(RPackage):
	"""Local Haplotype Clustering and Visualization

	A local haplotyping visualization toolbox to capture major patterns 
    of co-inheritance between clusters of linked variants, whilst connecting findings 
    to phenotypic and demographic traits across individuals. 'crosshap' enables users 
    to explore and understand genomic variation across a trait-associated region. 
    For an example of successful local haplotype analysis, see Marsh et al. (2022) 
    <doi:10.1007/s00122-022-04045-8>.
	"""
	
	homepage = "https://jacobimarsh.github.io/crosshap/"
	cran = "crosshap" 

	version("1.4.0", md5="31d988f22150470db4267e1997cd107f")
	version("1.2.2", md5="00e4e36dd0f70c75d92b79978f7922cb")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-clustree", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dbscan", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggdist", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
