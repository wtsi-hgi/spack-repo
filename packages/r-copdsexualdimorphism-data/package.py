# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopdsexualdimorphismData(RPackage):
    """Data to support sexually dimorphic and COPD differential analysis for gene expression and methylation.

    Datasets to support COPDSexaulDimorphism Package.
    """

    bioc = "COPDSexualDimorphism.data"

    version("1.44.0", commit="e6e8eabf02848bada04e950a11c2a76853228163")
    version("1.38.0", commit="7ca6bba8795310c24c381f0a05fc937522fcce51")
