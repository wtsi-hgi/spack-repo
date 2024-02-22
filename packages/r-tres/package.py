# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTres(RPackage):
	"""Tensor Regression with Envelope Structure

	Provides three estimators for tensor response regression (TRR) and tensor predictor regression (TPR) models with tensor envelope structure. The three types of estimation approaches are generic and can be applied to any envelope estimation problems. The full Grassmannian (FG) optimization is often associated with likelihood-based estimation but requires heavy computation and good initialization; the one-directional optimization approaches (1D and ECD algorithms) are faster, stable and does not require carefully chosen initial values; the SIMPLS-type is motivated by the partial least squares regression and is computationally the least expensive. For details of TRR, see Li L, Zhang X (2017) <doi:10.1080/01621459.2016.1193022>. For details of TPR, see Zhang X, Li L (2017) <doi:10.1080/00401706.2016.1272495>. For details of 1D algorithm, see Cook RD, Zhang X (2016) <doi:10.1080/10618600.2015.1029577>. For details of ECD algorithm, see Cook RD, Zhang X (2018) <doi:10.5705/ss.202016.0037>. For more details of the package, see Zeng J, Wang W, Zhang X (2021) <doi:10.18637/jss.v099.i12>.
	"""
	
	homepage = "https://github.com/leozeng15/TRES"
	cran = "TRES" 

	version("1.1.5", md5="1b860e9400afeaf34ac456049d7262a2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-manifoldoptim@1:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pracma@2.2.5:", type=("build", "run"))
	depends_on("r-rtensor@1.4:", type=("build", "run"))
