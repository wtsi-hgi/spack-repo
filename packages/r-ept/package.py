# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpt(RPackage):
	"""Ensemble Patch Transform, Visualization and Decomposition

	For multiscale analysis, this package carries out ensemble patch transform, its visualization and multiscale decomposition. The detailed procedure is described in Kim et al. (2020), and Oh and Kim (2020). D. Kim, G. Choi, H.-S. Oh, Ensemble patch transformation: a flexible framework for decomposition and filtering of signal, EURASIP Journal on Advances in Signal Processing 30 (2020) 1-27 <doi:10.1186/s13634-020-00690-7>. H.-S. Oh, D. Kim, Image decomposition by bidimensional ensemble patch transform, Pattern Recognition Letters 135 (2020) 173-179 <doi:10.1016/j.patrec.2020.03.029>.
	"""
	
	cran = "EPT" 

	version("0.7.6", md5="a7415a6068f3e32b82907464dbea06ad")

	depends_on("r@3:", type=("build", "run"))
