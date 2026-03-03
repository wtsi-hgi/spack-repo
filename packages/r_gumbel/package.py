# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGumbel(RPackage):
	"""The Gumbel-Hougaard Copula

	Provides probability functions (cumulative distribution and density functions), simulation function (Gumbel copula multivariate simulation) and estimation functions (Maximum Likelihood Estimation, Inference For Margins, Moment Based Estimation and Canonical Maximum Likelihood).
	"""
	
	cran = "gumbel" 

	version("1.10-2", md5="de6240fc57ad76837d2d13ae2cc8a41e")

	depends_on("r@2.10:", type=("build", "run"))
