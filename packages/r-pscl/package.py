# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPscl(RPackage):
    """Political Science Computational Laboratory.

    Bayesian analysis of item-response theory (IRT) models,
	roll call analysis; computing highest density regions; maximum
	likelihood estimation of zero-inflated and hurdle models for count
	data; goodness-of-fit measures for GLMs; data sets used
	in writing	and teaching at the Political Science
	Computational Laboratory; seats-votes curves."""

    cran = "pscl"

    version("1.5.5", sha256="054c9b88a991abdec3338688f58e81b6ba55f91edb988621864b24fd152fee6f")

    depends_on("r-mass", type=("build", "run"))
