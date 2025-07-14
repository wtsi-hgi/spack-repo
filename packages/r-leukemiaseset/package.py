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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/leukemiasEset_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/leukemiasEset/leukemiasEset_1.38.0.tar.gz"]

	version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="0bed1f20576d7184ab22184673fe05be2398e5c5d6bda4e6d43089e4f5b03ceb")

	depends_on("r@2.10.1:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

