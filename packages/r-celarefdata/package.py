# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCelarefdata(RPackage):
	"""Processed scRNA data for celaref Vignette - cell labelling by reference

	This experiment data contains some processed data used in the celaref package vignette. These are publically available datasets, that have been processed by celaref package, and can be manipulated further with it.
	"""
	
	bioc = "celarefData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/celarefData_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/celarefData/celarefData_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="48a454acc006d0de730c264e04c7b82c4f52dcf0f063b45ef7df69b92a2c7d87")

	depends_on("r@3.5:", type=("build", "run"))

