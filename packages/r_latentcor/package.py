# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatentcor(RPackage):
	"""Fast Computation of Latent Correlations for Mixed Data

	The first stand-alone R package for computation of latent correlation that takes into account all variable types (continuous/binary/ordinal/zero-inflated),
             comes with an optimized memory footprint, and is computationally efficient, essentially making latent correlation estimation almost as fast as rank-based correlation estimation.
             The estimation is based on latent copula Gaussian models.
             For continuous/binary types, see Fan, J., Liu, H., Ning, Y., and Zou, H. (2017).
             For ternary type, see Quan X., Booth J.G. and Wells M.T. (2018) <arXiv:1809.06255>.
             For truncated type or zero-inflated type, see Yoon G., Carroll R.J. and Gaynanova I. (2020) <doi:10.1093/biomet/asaa007>.
             For approximation method of computation, see Yoon G., Müller C.L. and Gaynanova I. (2021) <doi:10.1080/10618600.2021.1882468>. The latter method uses multi-linear interpolation originally implemented in the R package <https://cran.r-project.org/package=chebpol>.
	"""
	
	cran = "latentcor" 

	version("2.0.1", md5="1d20e1e193c6c51e3aa14457f0e74aef")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-fmultivar", type=("build", "run"))
	depends_on("r-mnormt", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-geometry", type=("build", "run"))
	depends_on("r-dofuture", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-microbenchmark", type=("build", "run"))
