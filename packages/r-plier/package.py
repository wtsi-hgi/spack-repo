# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlier(RPackage):
    """Implements the Affymetrix PLIER algorithm

    The PLIER (Probe Logarithmic Error Intensity Estimate) method produces an improved signal by accounting for experimentally observed patterns in probe behavior and handling error at the appropriately at low and high signal values.
    """

    bioc = "plier"

    version("1.78.0", commit="67fd95db6056806b32feaae5c5d61a7c5c0632a4")
    version("1.72.0", commit="a0a4265620a7c569ad4cb8cf0cd294ba28666a5f")

    depends_on("r@2:", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
