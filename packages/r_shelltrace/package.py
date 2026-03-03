# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShelltrace(RPackage):
	"""Bivalve Growth and Trace Element Accumulation Model

	
    Contains all the formulae of the growth and trace element uptake model described in the equally-named
    Geoscientific Model Development paper (de Winter, 2017, <doi:10.5194/gmd-2017-137>). The model takes as input a file with X- and Y-coordinates of digitized
    growth increments recognized on a longitudinal cross section through the bivalve shell, as well as a BMP file of an elemental map of the
    cross section surface with chemically distinct phases separated by phase analysis. It proceeds by a step-by-step process described in
    the paper, by which digitized growth increments are used to calculate changes in shell height, shell thickness, shell volume, shell mass
    and shell growth rate through the bivalve's life time. Then, results of this growth modelling are combined with the trace element mapping
    results to trace the incorporation of trace elements into the bivalve shell. Results of various modelling parameters can be exported in
    the form of XLSX files.
	"""
	
	homepage = "https://github.com/nielsjdewinter/ShellTrace"
	cran = "shelltrace" 

	version("3.5.1", md5="6933288533387a83c261e2331a5b4c4f")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
	depends_on("r-bmp", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
