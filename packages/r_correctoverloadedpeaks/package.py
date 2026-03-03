# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorrectoverloadedpeaks(RPackage):
	"""Correct Overloaded Peaks from GC-APCI-MS Data

	Analyzes and modifies metabolomics raw data (generated using GC-APCI-MS, Gas Chromatography-Atmospheric Pressure Chemical Ionization-Mass Spectrometry) to correct overloaded signals, i.e. ion intensities exceeding detector saturation leading to a cut-off peak. Data in xcmsRaw format are accepted as input and mzXML files can be processed alternatively. Overloaded signals are detected automatically and modified using an Gaussian or Isotopic-Ratio approach, QC plots are generated and corrected data are stored within the original xcmsRaw or mzXML respectively to allow further processing.
	"""
	
	homepage = "<doi:10.1021/acs.analchem.6b02515>"
	cran = "CorrectOverloadedPeaks" 

	version("1.3.3", md5="bfdb6a9e502c957fbbd7803a9934bbfd")

	depends_on("r@2.10:", type=("build", "run"))
