# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWdnet(RPackage):
	"""Weighted and Directed Networks

	Implementations of network analysis including
    (1) assortativity coefficient of weighted and directed networks, 
    Yuan, Yan and Zhang (2021) <doi:10.1093/comnet/cnab017>,
    (2) centrality measures for weighted and directed networks,
    Opsahl, Agneessens and Skvoretz (2010) <doi:10.1016/j.socnet.2010.03.006>,
    Zhang, Wang and Yan (2022) <doi:10.1016/j.physa.2021.126438>,
    (3) clustering coefficient of weighted and directed networks, 
    Fagiolo (2007) <doi:10.1103/PhysRevE.76.026107> and 
    Clemente and Grassi (2018) <doi:10.1016/j.chaos.2017.12.007>,
    (4) rewiring networks with given assortativity coefficients,
    Wang, Yan, Yuan and Zhang (2022) <doi:10.1007/s11222-022-10161-8>,
    (5) preferential attachment network generation,
    Yuan, Wang, Yan and Zhang (2023) <doi:10.6339/23-JDS1110>.
	"""
	
	homepage = "https://gitlab.com/wdnetwork/wdnet"
	cran = "wdnet" 

	version("1.2.2", md5="d46ae10a17728043025f15c9b8bbdcd4")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-cvxr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-rcppxptrutils", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
