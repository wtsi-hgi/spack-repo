# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpadrino(RPackage):
	"""Interact with the 'PADRINO' IPM Database

	'PADRINO' houses textual representations of
    Integral Projection Models which can be converted from their 
    table format into full kernels to reproduce or extend an 
    already published analysis. 'Rpadrino' is an R interface to this database. For
    more information on Integral Projection Models, see Easterling et al. (2000) 
  <doi:10.1890/0012-9658(2000)081[0694:SSSAAN]2.0.CO;2>, Merow et al. (2013) 
  <doi:10.1111/2041-210X.12146>, Rees et al. (2014) <doi:10.1111/1365-2656.12178>,
  and Metcalf et al. (2015) <doi:10.1111/2041-210X.12405>. See Levin et al. (2021)
  for more information on 'ipmr', the engine that powers model reconstruction
  <doi:10.1111/2041-210X.13683>.
	"""
	
	homepage = "https://github.com/padrinoDB/Rpadrino"
	cran = "Rpadrino" 

	version("0.0.5", md5="a717d81e879bf1e27bcf36de0294096e")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-ipmr@0.0.5:", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
	depends_on("curl", type=("build", "link", "run"))
