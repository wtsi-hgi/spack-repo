# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVocaldia(RPackage):
	"""Create and Manipulate Vocalisation Diagrams

	Create adjacency matrices of vocalisation graphs from
  dataframes containing sequences of speech and silence intervals,
  transforming these matrices into Markov diagrams, and generating
  datasets for classification of these diagrams by 'flattening' them
  and adding global properties (functionals) etc.  Vocalisation
  diagrams date back to early work in psychiatry (Jaffe and Feldstein,
  1970) and social psychology (Dabbs and Ruback, 1987) but have only
  recently been employed as a data representation method for machine
  learning tasks including meeting segmentation (Luz, 2012)
  <doi:10.1145/2328967.2328970> and classification (Luz,
  2013) <doi:10.1145/2522848.2533788>.
	"""
	
	homepage = "https://git.ecdf.ed.ac.uk/sluzfil/vocaldia"
	cran = "vocaldia" 

	version("0.8.4", md5="472cfd9f91413dfc5f585d69e9eb4941")

	depends_on("r@3:", type=("build", "run"))
