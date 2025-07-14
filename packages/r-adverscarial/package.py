# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdverscarial(RPackage):
	"""adverSCarial, generate and analyze the vulnerability of scRNA-seq classifiers to adversarial attacks

	adverSCarial is an R Package designed for generating and analyzing the vulnerability of scRNA-seq classifiers to adversarial attacks. The package is versatile and provides a format for integrating any type of classifier. It offers functions for studying and generating two types of attacks, single gene attack and max change attack. The single gene attack involves making a small modification to the input to alter the classification. The max change attack involves making a large modification to the input without changing its classification. The package provides a comprehensive solution for evaluating the robustness of scRNA-seq classifiers against adversarial attacks.
	"""
	
	bioc = "adverSCarial"

	version("1.6.0", commit="c0198fdae2d4ed11412c5f514d3d7f574568e1ea")
	version("1.0.0", commit="141ed014ac297989d1c0d6b9d26b4c782ac5ee2e")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
