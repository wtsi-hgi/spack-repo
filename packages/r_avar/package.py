# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAvar(RPackage):
	"""Allan Variance

	Implements the allan variance and allan variance linear regression estimator for latent time series models. More details about the method can be found, for example, in Guerrier, S., Molinari, R., & Stebler, Y. (2016) <doi:10.1109/LSP.2016.2541867>. 
	"""
	
	homepage = "https://github.com/SMAC-Group/avar"
	cran = "avar" 

	version("0.1.3", md5="a5976f3447f23917f91c3ec32aa3edc0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-simts", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
