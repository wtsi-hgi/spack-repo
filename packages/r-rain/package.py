# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRain(RPackage):
    """Rhythmicity Analysis Incorporating Non-parametric Methods

    This package uses non-parametric methods to detect rhythms in time series. It deals with outliers, missing values and is optimized for time series comprising 10-100 measurements. As it does not assume expect any distinct waveform it is optimal or detecting oscillating behavior (e.g. circadian or cell cycle) in e.g. genome- or proteome-wide biological measurements such as: micro arrays, proteome mass spectrometry, or metabolome measurements.
    """

    bioc = "rain"

    version("1.42.0", commit="e373710c9405b3df95df3589d069ce500848988e")
    version("1.36.0", commit="47311ae6751c2007b8034eb56aaf5a7d56f943d0")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-gmp", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
