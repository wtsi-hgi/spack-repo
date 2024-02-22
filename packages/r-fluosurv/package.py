# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFluosurv(RPackage):
	"""Estimate Insect Survival from Fluorescence Data

	Use spectrophotometry measurements performed on insects as a way to infer pathogens 
      virulence. Insect movements cause fluctuations in fluorescence signal, and functions are 
      provided to estimate when the insect has died as the moment when variance in autofluorescence 
      signal drops to zero. The package provides functions to obtain this estimate together with 
      functions to import spectrophotometry data from a Biotek microplate reader. Details of the method 
      are given in Parthuisot et al. (2018) <doi:10.1101/297929>.
	"""
	
	cran = "fluoSurv" 

	version("1.0.0", md5="23e530bf9f47ea00a272706c1f1a95f9")

	depends_on("r@3.1:", type=("build", "run"))
