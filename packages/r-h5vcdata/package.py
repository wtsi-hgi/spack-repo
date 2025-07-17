# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH5vcdata(RPackage):
    """Example data for the h5vc package

    This package contains the data used in the vignettes and examples of the 'h5vc' package
    """

    bioc = "h5vcData"

    version("2.28.0", commit="6b82461b6bb939ed833c20cde66be8b38416f6f5")
    version("2.22.0", commit="33c458b2a7f2687afbf050b8f211905f70cadf4e")
