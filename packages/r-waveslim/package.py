# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaveslim(RPackage):
	"""Basic Wavelet Routines for One-, Two-, and Three-Dimensional
Signal Processing

	Basic wavelet routines for time series (1D), image (2D) and array 
  (3D) analysis.  The code provided here is based on wavelet methodology 
  developed in Percival and Walden (2000); Gencay, Selcuk and Whitcher (2001); 
  the dual-tree complex wavelet transform (DTCWT) from Kingsbury (1999, 2001) as
  implemented by Selesnick; and Hilbert wavelet pairs (Selesnick 2001, 2002).  
  All figures in chapters 4-7 of GSW (2001) are reproducible using this package 
  and R code available at the book website(s) below.
	"""
	
	homepage = "https://waveslim.blogspot.com"
	cran = "waveslim" 

	version("1.8.4", md5="7af311a2567fd72a3080a2762aa1b929")

	depends_on("r@2.11:", type=("build", "run"))
