# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTinesath1cdf(RPackage):
    """tinesath1cdf

    A package containing an environment represeting the newcdf/tinesATH1.cdf.cdf file.
    """

    bioc = "tinesath1cdf"

    version("1.46.0", commit="d78c7a8e33b2b45603f0b061ba4badbaa72c4abd")
    version("1.40.0", commit="79fdbd5ab144ea2e631817d03f3d998244465e03")
