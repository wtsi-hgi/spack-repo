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

	version("1.24.0", commit="fa99172ecaf6f2df6be96e4c171ef75a6cdee78e")
	version("1.18.0", commit="ea93729f2fcc321564059eb8551b1174266e815d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-isocorrector", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
