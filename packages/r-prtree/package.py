# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrtree(RPackage):
	"""Probabilistic Regression Trees

	Probabilistic Regression Trees (PRTree). Functions for fitting and predicting PRTree models with some adaptations to handle missing values. The main calculations are performed in 'FORTRAN', resulting in highly efficient algorithms.
	This package's implementation is based on the PRTree methodology described in Alkhoury, S.; Devijver, E.; Clausel, M.; Tami, M.; Gaussier, E.; Oppenheim, G. (2020) - "Smooth And Consistent Probabilistic Regression Trees" <https://proceedings.neurips.cc/paper_files/paper/2020/file/8289889263db4a40463e3f358bb7c7a1-Paper.pdf>.
	"""
	
	cran = "PRTree" 

	version("0.1.0", md5="963af1839d45fbe4003cbb3c27cb28b4")

	depends_on("r@4.2:", type=("build", "run"))
