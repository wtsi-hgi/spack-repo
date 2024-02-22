# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLeukemiaseset(RPackage):
	"""Leukemia's microarray gene expression data (expressionSet).

	Expressionset containing gene expresion data from 60 bone marrow samples of patients with one of the four main types of leukemia (ALL, AML, CLL, CML) or non-leukemia.
	"""
	
	bioc = "leukemiasEset" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/leukemiasEset_1.38.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/leukemiasEset/leukemiasEset_1.38.0.tar.gz"]

	version("1.38.0", md5="f9e8274856b0d78de6da7ec0bce171f5")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

	# experiment