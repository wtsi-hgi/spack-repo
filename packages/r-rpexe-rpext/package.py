# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpexeRpext(RPackage):
	"""Reduced Piecewise Exponential Estimate/Test Software

	This reduced piecewise exponential survival software implements the likelihood ratio test and backward elimination procedure in Han, Schell, and Kim (2012 <doi:10.1080/19466315.2012.698945>, 2014 <doi:10.1002/sim.5915>), and Han et al. (2016 <doi:10.1111/biom.12590>). Inputs to the program can be either times when events/censoring occur or the vectors of total time on test and the number of events. Outputs of the programs are times and the corresponding p-values in the backward elimination. Details about the model and implementation are given in Han et al. 2014. This program can run in R version 3.2.2 and above.
	"""
	
	homepage = "https://github.com/hangangtrue/RPEXE.RPEXT"
	cran = "RPEXE.RPEXT" 

	version("0.0.2", md5="baa1d1d6e6b97a1797b9d6a05785aeb4")

	depends_on("r@3.2.2:", type=("build", "run"))
