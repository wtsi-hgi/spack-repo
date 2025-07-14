# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCuratedcrcdata(RPackage):
	"""Colorectal Cancer Gene Expression Analysis

	The curatedCRC package provides relevant functions and data for gene expression analysis in patients with colorectal cancer.
	"""
	
	homepage = "https://bitbucket.org/biobakery/curatedcrcdata"
	bioc = "curatedCRCData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/curatedCRCData_2.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/curatedCRCData/curatedCRCData_2.34.0.tar.gz"]

	version("2.40.0", tag="RELEASE_3_21")
	version("2.34.0", sha256="76f7fbb9b458472e3527ff92a03ee0dadf6ac662d77152606c2a104dff6d0cb7")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

