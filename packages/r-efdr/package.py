# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REfdr(RPackage):
	"""Wavelet-Based Enhanced FDR for Detecting Signals from Complete
or Incomplete Spatially Aggregated Data

	Enhanced False Discovery Rate (EFDR) is a tool to detect anomalies
    in an image. The image is first transformed into the wavelet domain in
    order to decorrelate any noise components, following which the coefficients
    at each resolution are standardised. Statistical tests (in a multiple
    hypothesis testing setting) are then carried out to find the anomalies. The
    power of EFDR exceeds that of standard FDR, which would carry out tests on
    every wavelet coefficient: EFDR choose which wavelets to test based on a
    criterion described in Shen et al. (2002). The package also provides
    elementary tools to interpolate spatially irregular data onto a grid of the
    required size. The work is based on Shen, X., Huang, H.-C., and Cressie, N.
    'Nonparametric hypothesis testing for a spatial signal.' Journal of the
    American Statistical Association 97.460 (2002): 1122-1140.
	"""
	
	homepage = "https://github.com/andrewzm/EFDR/"
	cran = "EFDR" 

	version("1.3", md5="f50fc5727dcfa8b709746e97745052d0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-foreach@1.4.2:", type=("build", "run"))
	depends_on("r-doparallel@1.0.8:", type=("build", "run"))
	depends_on("r-waveslim@1.7.5:", type=("build", "run"))
	depends_on("r-gstat@1.0.19:", type=("build", "run"))
	depends_on("r-tidyr@0.1.0.9000:", type=("build", "run"))
	depends_on("r-dplyr@0.3.0.2:", type=("build", "run"))
	depends_on("r-sp@1.0.15:", type=("build", "run"))
