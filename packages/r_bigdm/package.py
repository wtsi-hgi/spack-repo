# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigdm(RPackage):
	"""Scalable Bayesian Disease Mapping Models for High-Dimensional
Data

	Implements several spatial and spatio-temporal scalable disease mapping models for high-dimensional count data using the INLA technique for approximate Bayesian inference in latent Gaussian models (Orozco-Acosta et al., 2021 <doi:10.1016/j.spasta.2021.100496>; Orozco-Acosta et al., 2023 <doi:10.1016/j.cmpb.2023.107403> and Vicente et al., 2023 <doi:10.1007/s11222-023-10263-x>). The creation and develpment of this package has been supported by Project MTM2017-82553-R (AEI/FEDER, UE) and Project PID2020-113125RB-I00/MCIN/AEI/10.13039/501100011033. It has also been partially funded by the Public University of Navarra (project PJUPNA2001).
	"""
	
	homepage = "https://github.com/spatialstatisticsupna/bigDM"
	cran = "bigDM" 

	version("0.5.3", md5="c8bb14b1a4c2d55672c1e63535076eee")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-fastdummies", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-future-apply", type=("build", "run"))
	depends_on("r-geos", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-rlist", type=("build", "run"))
