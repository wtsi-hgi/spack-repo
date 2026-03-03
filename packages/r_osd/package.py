# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROsd(RPackage):
	"""Orthogonal Signal Deconvolution for Spectra Deconvolution in
GC-MS and GCxGC-MS Data

	Compound deconvolution for chromatographic data, including gas chromatography - mass spectrometry (GC-MS) and comprehensive gas chromatography - mass spectrometry (GCxGC-MS). The package includes functions to perform independent component analysis - orthogonal signal deconvolution (ICA-OSD), independent component regression (ICR), multivariate curve resolution (MCR-ALS) and orthogonal signal deconvolution (OSD) alone.
	"""
	
	cran = "osd" 

	version("0.1", md5="3059b42d390e3af0e8ec43d5f3cf7332")

	depends_on("r-jade", type=("build", "run"))
	depends_on("r-nnls", type=("build", "run"))
