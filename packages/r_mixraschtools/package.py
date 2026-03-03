# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMixraschtools(RPackage):
	"""Plotting and Average Theta Functions for Multiple Class Mixed
Rasch Models

	Provides supplemental functions for the 'mixRasch'
    package (Willse, 2014), <https://cran.r-project.org/package=mixRasch/mixRasch.pdf> including a 
    plotting function to compare item parameters for multiple
    class models and a function that provides average theta values for each class in
    a mixture model.
	"""
	
	cran = "mixRaschTools" 

	version("1.1.1", md5="c2a97dc0f9f8f7cf50e423cca459b336")

	depends_on("r@3.3:", type=("build", "run"))
