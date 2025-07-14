# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYeastrnaseq(RPackage):
	"""Yeast RNA-Seq Experimental Data from Lee et al. 2008

	A selection of RNA-Seq data from a yeast transcriptome experiment.
	"""
	
	bioc = "yeastRNASeq"

	version("0.46.0", commit="e03e84954c1a53caf365f8df822fc0d3d0cd8ccf")
	version("0.40.0", commit="57c93a0ad3c9a60c84572d094d30e026b75f1391")

	depends_on("r@2.4:", type=("build", "run"))

