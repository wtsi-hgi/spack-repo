# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCll(RPackage):
	"""A Package for CLL Gene Expression Data

	The CLL package contains the chronic lymphocytic leukemia (CLL) gene expression data.  The CLL data had 24 samples that were either classified as progressive or stable in regards to disease progression.  The data came from Dr. Sabina Chiaretti at Division of Hematology, Department of Cellular Biotechnologies and Hematology, University La Sapienza, Rome, Italy and Dr. Jerome Ritz at Department of Medicine, Brigham and Women's Hospital, Harvard Medical School, Boston, Massachusetts.
	"""
	
	bioc = "CLL" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CLL_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CLL/CLL_1.42.0.tar.gz"]

    version("1.48.0", tag="RELEASE_3_21")
	version("1.42.0", sha256="8e196bfa6d0648db1a7402e60cced90761a853f9c8efdab5181d1a2a4c518282")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-affy@1.23.4:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))

