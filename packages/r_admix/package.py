# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmix(RPackage):
	"""Package Admix for Admixture (aka Contamination) Models

	Implements techniques to estimate the unknown quantities related 
    to two-component admixture models, where the two components can belong to any
    distribution (note that in the case of multinomial mixtures, the two components
    must belong to the same family). Estimation methods depend on the assumptions 
    made on the unknown component density (see Bordes and Vandekerkhove (2010) <doi:10.3103/S1066530710010023>; 
    Patra and Sen (2016) <doi:10.1111/rssb.12148>); Milhaud, Pommeret, Salhi and Vandekerkhove 
    (2022) <doi:10.1016/j.jspi.2021.05.010>). In practice, one can estimate both the 
    mixture weight and the unknown component density in a wide variety of frameworks.
    On top of that, hypothesis tests can be performed in one and two-sample contexts 
    to test the unknown component density (see Milhaud, Pommeret, Salhi, Vandekerkhove (2023)).
    Finally, clustering of unknown mixture components is also feasible in a K-samples setting.
	"""
	
	homepage = "https://github.com/XavierMilhaud/admix"
	cran = "admix" 

	version("2.1-2", md5="23f0cca4a9f90fb2f64f6df95b1342d1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-fdrtool", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-orthopolynom", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
