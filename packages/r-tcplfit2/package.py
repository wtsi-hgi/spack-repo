# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcplfit2(RPackage):
	"""Concentration-Response Modeling of HTS or Transcriptomics Data

	Performs the basic concentration response curve fitting used 
    in the 'tcpl' package. It is a substitute for the original tcplFit() function 
    (and sub-functions) and allows a wider variety of concentration-response models. 
    All of the models included in the 'BMDExpress' package are now part of this package,
    and the output includes a calculation of the bmd (Benchmark Dose or concentration) 
    value.
	"""
	
	cran = "tcplfit2" 

	version("0.1.6", md5="6396627cae51ca42b75eedca748e1c9d", url="https://cran.r-project.org/src/contrib/tcplfit2_0.1.6.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
