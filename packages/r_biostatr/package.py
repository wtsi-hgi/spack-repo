# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiostatr(RPackage):
	"""Initiation à La Statistique Avec R

	Datasets and functions for the book "Initiation à la Statistique avec R", F. Bertrand and M. Maumy-Bertrand (2022, ISBN:978-2100782826 Dunod, fourth edition).
	"""
	
	homepage = "https://fbertran.github.io/BioStatR/"
	cran = "BioStatR" 

	version("4.0.1", md5="8f72dad0d9481514b71348349924282f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
