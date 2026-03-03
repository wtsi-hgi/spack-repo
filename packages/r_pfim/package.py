# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPfim(RPackage):
	"""Population Fisher Information Matrix

	Evaluate or optimize designs for nonlinear mixed effects models using the Fisher Information matrix. Methods used in the package refer to 
    Mentré F, Mallet A, Baccar D (1997) <doi:10.1093/biomet/84.2.429>,
    Retout S, Comets E, Samson A, Mentré F (2007) <doi:10.1002/sim.2910>,
    Bazzoli C, Retout S, Mentré F (2009) <doi:10.1002/sim.3573>,
    Le Nagard H, Chao L, Tenaillon O (2011) <doi:10.1186/1471-2148-11-326>,
    Combes FP, Retout S, Frey N, Mentré F (2013) <doi:10.1007/s11095-013-1079-3> and
    Seurat J, Tang Y, Mentré F, Nguyen TT (2021) <doi:10.1016/j.cmpb.2021.106126>.
	"""
	
	homepage = "http://www.pfim.biostat.fr/"
	cran = "PFIM" 

	version("6.0.3", md5="71632c7b601003f46671ce29ef5733c7")
	version("6.0.2", md5="e241f9032d1ee07cd8bda510fff04ec7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-deriv", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
