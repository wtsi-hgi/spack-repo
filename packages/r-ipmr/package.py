# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpmr(RPackage):
	"""Integral Projection Models

	Flexibly implements Integral Projection Models using a
  mathematical(ish) syntax. This package will not help with the vital rate
  modeling process, but will help convert those regression models into an
  IPM. 'ipmr' handles density dependence and environmental stochasticity, with a
  couple of options for implementing the latter. In addition, provides functions
  to avoid unintentional eviction of individuals from models. Additionally, 
  provides model diagnostic tools, plotting functionality, 
  stochastic/deterministic simulations, and analysis tools.
  Integral projection models are described in depth by Easterling et al. (2000) 
  <doi:10.1890/0012-9658(2000)081[0694:SSSAAN]2.0.CO;2>, Merow et al. (2013) 
  <doi:10.1111/2041-210X.12146>, Rees et al. (2014) <doi:10.1111/1365-2656.12178>,
  and Metcalf et al. (2015) <doi:10.1111/2041-210X.12405>. 
  Williams et al. (2012) <doi:10.1890/11-2147.1> discuss the problem of 
  unintentional eviction.
	"""
	
	homepage = "https://padrinoDB.github.io/ipmr/"
	cran = "ipmr" 

	version("0.0.7", md5="0bbc947744f2f5ecd31eb97266463521")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr@0.3:", type=("build", "run"))
	depends_on("r-rlang@0.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
