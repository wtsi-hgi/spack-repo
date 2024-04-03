# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParam2moment(RPackage):
	"""Raw, Central and Standardized Moments of Parametric
Distributions

	To calculate the raw, central and
      standardized moments from distribution parameters.
      To solve the distribution parameters based on
      user-provided mean, standard deviation, skewness
      and kurtosis. Normal, skew-normal, skew-t and
      Tukey g-&-h distributions are supported, for now.
	"""
	
	cran = "param2moment" 

	version("0.1.0", md5="36aa30d9814951807df4acdd3deabebc")

	depends_on("r@4.3:", type=("build", "run"))
