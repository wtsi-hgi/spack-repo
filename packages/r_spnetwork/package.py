# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpnetwork(RPackage):
	"""Spatial Analysis on Network

	Perform spatial analysis on network.
    Implement several methods for spatial analysis on network: Network Kernel Density estimation, 
    building of spatial matrices based on network distance ('listw' objects from 'spdep' package), K functions estimation 
    for point pattern analysis on network, k nearest neighbours on network, reachable area calculation, and graph generation
    References: Okabe et al (2019) <doi:10.1080/13658810802475491>;
    Okabe et al (2012, ISBN:978-0470770818);Baddeley et al (2015, ISBN:9781482210200).
	"""
	
	homepage = "https://jeremygelb.github.io/spNetwork/"
	cran = "spNetwork" 

	version("0.4.3.8", md5="a27718c248888de4eef3d17154c8cef5")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-spdep@1.1.2:", type=("build", "run"))
	depends_on("r-igraph@1.2.6:", type=("build", "run"))
	depends_on("r-cubature@2.0.4.1:", type=("build", "run"))
	depends_on("r-future-apply@1.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-progressr@0.4:", type=("build", "run"))
	depends_on("r-data-table@1.12.8:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rdpack@2.1.1:", type=("build", "run"))
	depends_on("r-dbscan@1.1.8:", type=("build", "run"))
	depends_on("r-sf@1.0.3:", type=("build", "run"))
	depends_on("r-dplyr@0.8.3:", type=("build", "run"))
	depends_on("r-abind@1.4.5:", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
