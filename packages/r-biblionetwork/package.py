# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiblionetwork(RPackage):
	"""Create Different Types of Bibliometric Networks

	Functions to find edges for bibliometric networks like bibliographic coupling network, co-citation network and co-authorship network. The weights of network edges can be calculated according to different methods, depending on the type of networks, the type of nodes, and what you want to analyse. These functions are optimized to be be used on large dataset. The package contains functions inspired by: Leydesdorff, Loet and Park, Han Woo (2017) <doi:10.1016/j.joi.2016.11.007>; Perianes-Rodriguez, Antonio, Ludo Waltman, and Nees Jan Van Eck (2016) <doi:10.1016/j.joi.2016.10.006>; Sen, Subir K. and Shymal K. Gan (1983) <http://nopr.niscair.res.in/handle/123456789/28008>; Shen, Si, Zhu, Danhao, Rousseau, Ronald, Su, Xinning and Wang, Dongbo (2019) <doi:10.1016/j.joi.2019.01.012>; Zhao, Dangzhi and Strotmann, Andreas (2008) <doi:10.1002/meet.2008.1450450292>.
	"""
	
	homepage = "https://github.com/agoutsmedt/biblionetwork"
	cran = "biblionetwork" 

	version("0.1.0", md5="b221d185a51c22795663e739285c6b8e")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rdpack@0.7:", type=("build", "run"))
