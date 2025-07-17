# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSizepower(RPackage):
    """Sample Size and Power Calculation in Micorarray Studies

    This package has been prepared to assist users in computing either a sample size or power value for a microarray experimental study. The user is referred to the cited references for technical background on the methodology underpinning these calculations. This package provides support for five types of sample size and power calculations. These five types can be adapted in various ways to encompass many of the standard designs encountered in practice.
    """

    bioc = "sizepower"

    version("1.78.0", commit="33f14e42127e499125204177a57a9224d3eab0eb")
    version("1.72.0", commit="c6912dc1793245c280a7e240e34849c618ce32ec")
