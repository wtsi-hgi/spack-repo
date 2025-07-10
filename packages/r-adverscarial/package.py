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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/adverSCarial_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/adverSCarial/adverSCarial_1.0.0.tar.gz"]

	version("1.0.0", sha256="0a6c0c8d2d9567c14040c9be8db7f89c0704df3dd143f63bb5b71fdf6828cdfa")

	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
