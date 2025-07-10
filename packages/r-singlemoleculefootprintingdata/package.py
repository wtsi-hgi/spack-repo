# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSinglemoleculefootprintingdata(RPackage):
	"""Data supporting the SingleMoleculeFootprinting pkg

	This Data package contains data objcets relevanat for the SingleMoleculeFootprinting package. More specifically, it contains one example of aligned sequencing data (.bam & .bai) necessary to run the SingleMoleculeFootprinting vignette. Additionally, we provide data that are essential for some functions to work correctly such as BaitCapture() and SampleCorrelation().
	"""
	
	bioc = "SingleMoleculeFootprintingData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/SingleMoleculeFootprintingData_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/SingleMoleculeFootprintingData/SingleMoleculeFootprintingData_1.10.0.tar.gz"]

	version("1.10.0", sha256="039c4c9dd29362af9931c6478b49748ac8d9cba237ced8f7043c6ae6d18c14b2")

	depends_on("r-experimenthub", type=("build", "run"))

