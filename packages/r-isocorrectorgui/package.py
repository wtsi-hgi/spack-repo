# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsocorrectorgui(RPackage):
	"""Graphical User Interface for IsoCorrectoR

	IsoCorrectoRGUI is a Graphical User Interface for the IsoCorrectoR package. IsoCorrectoR performs the correction of mass spectrometry data from stable isotope labeling/tracing metabolomics experiments with regard to natural isotope abundance and tracer impurity. Data from both MS and MS/MS measurements can be corrected (with any tracer isotope: 13C, 15N, 18O...), as well as high resolution MS data from multiple-tracer experiments (e.g. 13C and 15N used simultaneously).
	"""
	
	homepage = "https://genomics.ur.de/files/IsoCorrectoRGUI"
	bioc = "IsoCorrectoRGUI" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/IsoCorrectoRGUI_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/IsoCorrectoRGUI/IsoCorrectoRGUI_1.18.0.tar.gz"]

	version("1.18.0", md5="2f46ff7c7647616cced839067b9e1b39")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-isocorrector", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
