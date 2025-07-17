# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetamsdata(RPackage):
    """Example CDF data for the metaMS package

    Example CDF data for the metaMS package
    """

    bioc = "metaMSdata"

    version("1.44.0", commit="9ba3cd2715e8a547a5dcf7d881bd2c8aaa0bdf60")
    version("1.38.0", commit="cdf4625580bc71c1cce2064917f65b4d30699eb3")
