# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPedigreetools(RPackage):
	"""Versatile Functions for Working with Pedigrees

	Tools to sort, edit and prune pedigrees and to extract the inbreeding coefficients
    and the relationship matrix (includes code for pedigrees from self-pollinated species). 
    The use of pedigree data is central to genetics research within the animal and plant breeding communities to predict 
    breeding values. The relationship matrix between the individuals can be derived from pedigree structure 
    ('Vazquez et al., 2010') <doi:10.2527/jas.2009-1952>.
	"""
	
	homepage = "https://github.com/Rpedigree/pedigreeTools/"
	cran = "pedigreeTools" 

	version("0.2", md5="055f3d8d14be0430db37085e38aa946c")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-matrix@1:", type=("build", "run"))
