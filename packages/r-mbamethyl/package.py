# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbamethyl(RPackage):
    """Model-based analysis of DNA methylation data

    This package provides a function for reconstructing DNA methylation values from raw measurements. It iteratively implements the group fused lars to smooth related-by-location methylation values and the constrained least squares to remove probe affinity effect across multiple sequences.
    """

    bioc = "MBAmethyl"

    version("1.42.0", commit="32f32b8cb08c51109005e49e644e4d817e09367f")
    version("1.36.0", commit="70df0ef0010be22ec14504540e6f0a971bcadf84")

    depends_on("r@2.15:", type=("build", "run"))
