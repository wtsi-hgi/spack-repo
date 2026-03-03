# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocnreg(RPackage):
	"""ROC Curve Inference with and without Covariates

	Estimates the pooled (unadjusted) Receiver Operating Characteristic (ROC) curve, the covariate-adjusted ROC (AROC) curve, and the covariate-specific/conditional ROC (cROC) curve by different methods, both Bayesian and frequentist. Also, it provides functions to obtain ROC-based optimal cutpoints utilizing several criteria. Based on Erkanli, A. et al. (2006) <doi:10.1002/sim.2496>; Faraggi, D. (2003) <doi:10.1111/1467-9884.00350>; Gu, J. et al. (2008) <doi:10.1002/sim.3366>; Inacio de Carvalho, V. et al. (2013) <doi:10.1214/13-BA825>; Inacio de Carvalho, V., and Rodriguez-Alvarez, M.X. (2018) <arXiv:1806.00473>; Janes, H., and Pepe, M.S. (2009) <doi:10.1093/biomet/asp002>; Pepe, M.S. (1998) <http://www.jstor.org/stable/2534001?seq=1>; Rodriguez-Alvarez, M.X. et al. (2011a) <doi:10.1016/j.csda.2010.07.018>; Rodriguez-Alvarez, M.X. et al. (2011a) <doi:10.1007/s11222-010-9184-1>. Please see Rodriguez-Alvarez, M.X. and Inacio, V. (20208) <arXiv:2003.13111> for more details.
	"""
	
	cran = "ROCnReg" 

	version("1.0-8", md5="3d9f5089fc9981f019bd2c5c5c819174")

	depends_on("r-np", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-spatstat-geom", type=("build", "run"))
	depends_on("r-spatstat@2.0.0:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbivnorm", type=("build", "run"))
