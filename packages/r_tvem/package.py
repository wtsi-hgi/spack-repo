# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTvem(RPackage):
	"""Time-Varying Effect Models

	Fits time-varying effect models (TVEM). These are a kind of application of varying-coefficient models in the context of longitudinal data, allowing the strength of linear, logistic, or Poisson regression relationships to change over time.  These models are described further in Tan, Shiyko, Li, Li & Dierker (2012) <doi:10.1037/a0025814>.  We thank Kaylee Litson, Patricia Berglund, Yajnaseni Chakraborti, and Hanjoo Kim for their valuable help with testing the package and the documentation. The development of this package was part of a research project supported by National Institutes of Health grants P50 DA039838 from the National Institute of Drug Abuse and 1R01 CA229542-01 from the National Cancer Institute and the NIH Office of Behavioral and Social Science Research. Content is solely the responsibility of the authors and does not necessarily represent the official views of the funding institutions mentioned above. This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
	"""
	
	cran = "tvem" 

	version("1.4.1", md5="d8a6714f43c899570d67ff71ee712476")

	depends_on("r-mgcv", type=("build", "run"))
