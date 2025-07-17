# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMassspecwavelet(RPackage):
    """Peak Detection for Mass Spectrometry data using wavelet-based algorithms

    Peak Detection in Mass Spectrometry data is one of the important preprocessing steps. The performance of peak detection affects subsequent processes, including protein identification, profile alignment and biomarker identification. Using Continuous Wavelet Transform (CWT), this package provides a reliable algorithm for peak detection that does not require any type of smoothing or previous baseline correction method, providing more consistent results for different spectra. See <doi:10.1093/bioinformatics/btl355} for further details.
    """

    homepage = "https://github.com/zeehio/MassSpecWavelet"
    bioc = "MassSpecWavelet"

    version("1.74.0", commit="e19b8a04fc7271f17b6d3213a303d5efc67c2079")
    version("1.68.0", commit="99ece70aaf0380ab545f259241724ffe10c7b727")
