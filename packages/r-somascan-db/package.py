# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSomascanDb(RPackage):
	"""Somalogic SomaScan Annotation Data

	An R package providing extended biological annotations for the SomaScan Assay, a proteomics platform developed by SomaLogic Operating Co., Inc. The annotations in this package were assembled using data from public repositories. For more information about the SomaScan assay and its data, please reference the 'SomaLogic/SomaLogic-Data' GitHub repository.
	"""
	
	homepage = "https://somalogic.com"
	bioc = "SomaScan.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/SomaScan.db_0.99.7.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/SomaScan.db/SomaScan.db_0.99.7.tar.gz"]

	version("0.99.7", md5="aa52f4f12dfb2f0aa4c7fe3633de4646")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-annotationdbi@1.56.2:", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.14:", type=("build", "run"))

