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

	version("1.24.0", tag="RELEASE_3_21")
	version("1.18.0", sha256="9953d5aa15a6c18f898f4533e83d395b0c7e2121d22f2f9fb0a6c5e0c14cd7c0")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-isocorrector", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
