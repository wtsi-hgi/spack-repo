# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeurosim(RPackage):
	"""Simulate fMRI Data

	Generates functional Magnetic Resonance Imaging (fMRI) 
             time series or 4D data. Some high-level 
             functions are created for fast data generation with only 
             a few arguments and a diversity of functions to define 
             activation and noise. For more advanced users it is possible 
             to use the low-level functions and manipulate the arguments.
             See Welvaert et al. (2011) <doi:10.18637/jss.v044.i10>.
	"""
	
	cran = "neuRosim" 

	version("0.2-14", md5="1776c1111cb80054266cc1ca2adf9166")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
