# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtdists(RPackage):
	"""Response Time Distributions

	Provides response time distributions (density/PDF,
       distribution function/CDF, quantile function, and random
       generation): (a) Ratcliff diffusion model (Ratcliff &
       McKoon, 2008, <doi:10.1162/neco.2008.12-06-420>) based on C
       code by Andreas and Jochen Voss and (b) linear ballistic
       accumulator (LBA; Brown & Heathcote, 2008,
       <doi:10.1016/j.cogpsych.2007.12.002>) with different
       distributions underlying the drift rate.
	"""
	
	homepage = "https://github.com/rtdists/rtdists/"
	cran = "rtdists" 

	version("0.11-5", md5="dff39ce10b8650353fddbcf70a3c0252")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-evd", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-gsl", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
