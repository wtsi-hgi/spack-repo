# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFmx(RPackage):
	"""Finite Mixture Parametrization

	A parametrization framework for finite mixture
      distribution using S4 objects. Density, cumulative
      density, quantile and simulation functions are
      defined. Currently normal, Tukey g-&-h, skew-normal
      and skew-t distributions are well tested. The gamma,
      negative binomial distributions are being tested.
	"""
	
	cran = "fmx" 

	version("0.1.0", md5="d0e14eed762365ebc24909704b2738ae")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-goftest", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-tukeygh77", type=("build", "run"))
	depends_on("r-vgam", type=("build", "run"))
