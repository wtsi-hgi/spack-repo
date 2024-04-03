# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPafit(RPackage):
	"""Generative Mechanism Estimation in Temporal Complex Networks

	Statistical methods for estimating preferential attachment and node fitness generative mechanisms in temporal complex networks are provided. Thong Pham et al. (2015) <doi:10.1371/journal.pone.0137796>. Thong Pham et al. (2016) <doi:10.1038/srep32558>. Thong Pham et al. (2020) <doi:10.18637/jss.v092.i03>. Thong Pham et al. (2021) <doi:10.1093/comnet/cnab024>.  
	"""
	
	homepage = "https://github.com/thongphamthe/PAFit"
	cran = "PAFit" 

	version("1.2.10", md5="8df4ce7a608a689d1194496c449ea068")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-magicaxis", type=("build", "run"))
	depends_on("r-networkdynamic", type=("build", "run"))
	depends_on("r-network", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
