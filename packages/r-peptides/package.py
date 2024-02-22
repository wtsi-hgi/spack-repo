# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPeptides(RPackage):
	"""Calculate Indices and Theoretical Physicochemical Properties of
Protein Sequences

	Includes functions to calculate several physicochemical properties and indices for amino-acid sequences as well as to read and plot 'XVG' output files from the 'GROMACS' molecular dynamics package.
	"""
	
	homepage = "https://github.com/dosorio/Peptides/"
	cran = "Peptides" 

	version("2.4.6", md5="0777b1940686a03ec7f98301136fda77")

	depends_on("r-rcpp", type=("build", "run"))
