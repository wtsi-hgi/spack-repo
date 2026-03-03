# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBigmds(RPackage):
	"""Multidimensional Scaling for Big Data

	MDS is a statistic tool for reduction of dimensionality, using as input a distance
    matrix of dimensions n × n. When n is large, classical algorithms suffer from
    computational problems and MDS configuration can not be obtained.
    With this package, we address these problems by means of six algorithms, being two of them 
    original proposals:
        - Landmark MDS proposed by De Silva V. and JB. Tenenbaum (2004).
        - Interpolation MDS proposed by Delicado P. and C. Pachón-García (2021)
        <arXiv:2007.11919> (original proposal).
        - Reduced MDS proposed by Paradis E (2018).
        - Pivot MDS proposed by Brandes U. and C. Pich (2007)
        - Divide-and-conquer MDS proposed by Delicado P. and C. Pachón-García (2021)
        <arXiv:2007.11919> (original proposal).
        - Fast MDS, proposed by Yang, T., J. Liu, L. McMillan and W. Wang (2006).
	"""
	
	homepage = "https://github.com/pachoning/bigmds"
	cran = "bigmds" 

	version("3.0.0", md5="c7b9ca1e803e551bfa03cf3afd6a87a2")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-svd", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
