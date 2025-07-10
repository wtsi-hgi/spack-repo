# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFabiadata(RPackage):
	"""Data sets for FABIA (Factor Analysis for Bicluster Acquisition)

	Supplying gene expression data sets for the demos of the biclustering method "Factor Analysis for Bicluster Acquisition" (FABIA). The following three data sets are provided: A) breast cancer (van't Veer, Nature, 2002), B) multiple tissues (Su, PNAS, 2002), and C) diffuse large-B-cell lymphoma (Rosenwald, N Engl J Med, 2002).
	"""
	
	homepage = "http://www.bioinf.jku.at/software/fabia/fabia.html"
	bioc = "fabiaData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/fabiaData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/fabiaData/fabiaData_1.40.0.tar.gz"]

	version("1.40.0", sha256="bb517c14c8596f0d02ccdbfd0156274b72a49c32f20420e48dd9c87d6608902a")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))

