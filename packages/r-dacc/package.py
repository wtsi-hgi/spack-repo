# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDacc(RPackage):
	"""Detection and Attribution Analysis of Climate Change

	
    Conduct detection and attribution of climate change using methods including optimal fingerprinting via 
    generalized total least squares or estimating equation approach from Ma et al. (2023) <doi:10.1175/JCLI-D-22-0681.1>. 
    Provide shrinkage estimators for covariance matrix from Ledoit and Wolf (2004) <doi:10.1016/S0047-259X(03)00096-4>, 
    and Ledoit and Wolf (2017) <doi:10.2139/ssrn.2383361>.
	"""
	
	homepage = "https://github.com/LiYanStat/dacc"
	cran = "dacc" 

	version("0.0-3", md5="b9b056d9dcac18e2ee59c7bddce81051")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-janitor", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
