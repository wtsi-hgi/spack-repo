# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmd(RPackage):
	"""Empirical Mode Decomposition and Hilbert Spectral Analysis

	For multiscale analysis, this package carries out empirical mode decomposition and Hilbert spectral
        analysis. For usage of EMD, see Kim and Oh, 2009 (Kim, D and Oh, H.-S. (2009) EMD: A Package for Empirical 
        Mode Decomposition and Hilbert Spectrum, The R Journal, 1, 40-46). 
	"""
	
	cran = "EMD" 

	version("1.5.9", md5="cb85f508af05d4a7b5e1d5b1c1ea2f44")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-fields@6.9.1:", type=("build", "run"))
	depends_on("r-locfit@1.5.8:", type=("build", "run"))
