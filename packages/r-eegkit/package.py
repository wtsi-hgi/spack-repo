# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REegkit(RPackage):
	"""Toolkit for Electroencephalography Data

	Analysis and visualization tools for electroencephalography (EEG) data. Includes functions for (i) plotting EEG data, (ii) filtering EEG data, (iii) smoothing EEG data; (iv) frequency domain (Fourier) analysis of EEG data, (v) Independent Component Analysis of EEG data, and (vi) simulating event-related potential EEG data.
	"""
	
	cran = "eegkit" 

	version("1.0-4", md5="554b5968d5ccb101b9ba4b98744be301")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-eegkitdata", type=("build", "run"))
	depends_on("r-bigsplines", type=("build", "run"))
	depends_on("r-ica", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
