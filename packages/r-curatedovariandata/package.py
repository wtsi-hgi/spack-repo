# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedovariandata(RPackage):
	"""Clinically Annotated Data for the Ovarian Cancer Transcriptome

	The curatedOvarianData package provides data for gene expression analysis in patients with ovarian cancer.
	"""
	
	homepage = "http://bcb.dfci.harvard.edu/ovariancancer"
	bioc = "curatedOvarianData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/curatedOvarianData_1.40.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/curatedOvarianData/curatedOvarianData_1.40.1.tar.gz"]

	version("1.40.1", sha256="4ab9aed6d1f643f266c5b3b57c36ba74a8d8ab1e24fc87451504bcf1001d26a0")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

