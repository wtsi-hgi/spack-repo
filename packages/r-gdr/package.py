# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGdr(RPackage):
    """Umbrella package for R packages in the gDR suite

    Package is a part of the gDR suite. It reexports functions from other packages in the gDR suite that contain critical processing functions and utilities. The vignette walks through the full processing pipeline for drug response analyses that the gDR suite offers.
    """

    bioc = "gDR"

    version("1.6.0", commit="415ca31b1beefb5374672d71b476cf862e2c0fa2")
    version("1.0.0", commit="3b047b8962172654687ec093f75f861f65df0a92")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-gdrcore@0.99.12:", type=("build", "run"))
    depends_on("r-gdrimport@0.99.10:", type=("build", "run"))
    depends_on("r-gdrutils@0.99.13:", type=("build", "run"))
