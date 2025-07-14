# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTcgabiolinksguiData(RPackage):
	"""Data for the TCGAbiolinksGUI package

	Supporting data for the TCGAbiolinksGUI package.
	"""
	
	homepage = "https://github.com/BioinformaticsFMRP/TCGAbiolinksGUI.data"
	bioc = "TCGAbiolinksGUI.data" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/TCGAbiolinksGUI.data_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/TCGAbiolinksGUI.data/TCGAbiolinksGUI.data_1.22.0.tar.gz"]

    version("1.28.0", tag="RELEASE_3_21")
	version("1.22.0", sha256="cad5d078da2d9df521a4bc5398324849caf4d73c6d3c46dda362e59214b6d511")

	depends_on("r@3.5:", type=("build", "run"))

