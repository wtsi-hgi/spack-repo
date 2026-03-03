# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmam(RPackage):
	"""Statistical Modeling of Animal Movements

	Animal movement models including Moving-Resting Process
    with Embedded Brownian Motion
    (Yan et al., 2014, <doi:10.1007/s10144-013-0428-8>;
    Pozdnyakov et al., 2017, <doi:10.1007/s11009-017-9547-6>),
    Brownian Motion with Measurement Error
    (Pozdnyakov et al., 2014, <doi:10.1890/13-0532.1>),
    Moving-Resting-Handling Process with Embedded Brownian Motion
    (Pozdnyakov et al., 2020, <doi:10.1007/s11009-020-09774-1>),
    Moving-Resting Process with Measurement Error
    (Hu et al., 2021, <doi:10.1111/2041-210X.13694>),
    Moving-Moving Process with two Embedded Brownian Motions.
	"""
	
	homepage = "https://github.com/ChaoranHu/smam"
	cran = "smam" 

	version("0.7.2", md5="b963f76179433aa186725265e6e4b0b8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dosnow", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-rcppgsl", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
