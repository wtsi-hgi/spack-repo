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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MassSpecWavelet_1.68.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MassSpecWavelet/MassSpecWavelet_1.68.0.tar.gz"]

	version("1.74.0", tag="RELEASE_3_21")
	version("1.68.0", sha256="5ea71adfc8e632ab10c5b208572e398a1fc799b01d02a1608a688bafbbf89910")

