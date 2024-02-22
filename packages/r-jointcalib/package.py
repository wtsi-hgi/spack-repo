# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointcalib(RPackage):
	"""A Joint Calibration of Totals and Quantiles

	A small package containing functions to perform a joint calibration of totals and quantiles. The calibration for totals is based on Deville and Särndal (1992) <doi:10.1080/01621459.1992.10475217>, the calibration for quantiles is based on Harms and Duchesne (2006) <https://www150.statcan.gc.ca/n1/en/catalogue/12-001-X20060019255>. The package uses standard calibration via the 'survey', 'sampling' or 'laeken' packages. In addition, entropy balancing via the 'ebal' package and empirical likelihood based on codes from Wu (2005) <https://www150.statcan.gc.ca/n1/pub/12-001-x/2005002/article/9051-eng.pdf> can be used. See the paper by Beręsewicz and Szymkowiak (2023) for details <arXiv:2308.13281>.
	"""
	
	homepage = "https://github.com/ncn-foreigners/jointCalib"
	cran = "jointCalib" 

	version("0.1.0", md5="da0defaf45c42991f031929f1cf4d5f8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-laeken", type=("build", "run"))
	depends_on("r-sampling", type=("build", "run"))
	depends_on("r-mathjaxr", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ebal", type=("build", "run"))
