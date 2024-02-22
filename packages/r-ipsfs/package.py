# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIpsfs(RPackage):
	"""Intuitionistic, Pythagorean, and Spherical Fuzzy Similarity
Measure

	Advanced fuzzy logic based techniques are implemented to compute the similarity among different objects or items. Typically, application areas consist of transforming raw data into the corresponding advanced fuzzy logic representation and determining the similarity between two objects using advanced fuzzy similarity techniques in various fields of research, such as text classification, pattern recognition, software projects, decision-making, medical diagnosis, and market prediction. Functions are designed to compute the membership, non-membership, hesitant-membership, indeterminacy-membership, and refusal-membership for the input matrices. Furthermore, it also includes a large number of advanced fuzzy logic based similarity measure functions to compute the Intuitionistic fuzzy similarity (IFS), Pythagorean fuzzy similarity (PFS), and Spherical fuzzy similarity (SFS) between two objects or items based on their fuzzy relationships. It also includes working examples for each function with sample data sets.
	"""
	
	cran = "ipsfs" 

	version("1.0.0", md5="2a21d10c43eb429e4a7af3c832fa1491")

