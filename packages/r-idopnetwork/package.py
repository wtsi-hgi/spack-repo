# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdopnetwork(RPackage):
	"""A Network Tool to Dissect Spatial Community Ecology

	Most existing approaches for network reconstruction can only infer an overall network 
	and, also, fail to capture a complete set of network properties. To address these issues, 
	a new model has been developed, which converts static data into their 'dynamic' form. 
	'idopNetwork' is an 'R' interface to this model, it can inferring informative, dynamic, 
	omnidirectional and personalized networks. For more information on functional 
	clustering part, see Kim et al. (2008) <doi:10.1534/genetics.108.093690>, 
	Wang et al. (2011) <doi:10.1093/bib/bbr032>. For more information on our model, 
	see Chen et al. (2019) <doi:10.1038/s41540-019-0116-1>, and Cao et al. (2022) 
	<doi:10.1080/19490976.2022.2106103>.
	"""
	
	homepage = "https://github.com/cxzdsa2332/idopNetwork"
	cran = "idopNetwork" 

	version("0.1.2", md5="675815e30165f06ecd56ffeb7b439d32")

	depends_on("r@3.50:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
