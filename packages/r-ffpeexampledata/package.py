# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFfpeexampledata(RPackage):
	"""Illumina DASL example microarray data

	A subset of GSE17565 (April et al. 2009) containing 32 FFPE samples of Burkitts Lymphoma and Breast Adenocarcinoma, with a dilution series in technical duplicate.
	"""
	
	bioc = "ffpeExampleData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ffpeExampleData_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ffpeExampleData/ffpeExampleData_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="d977b80375a09d65d1950871bb166b7ec29cefe3e1a06a1cfdf01c0bbab87d99")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-lumi", type=("build", "run"))

