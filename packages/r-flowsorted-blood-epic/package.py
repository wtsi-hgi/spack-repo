# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedBloodEpic(RPackage):
	"""Illumina EPIC data on immunomagnetic sorted peripheral adult blood cells

	Raw data objects to be used for blood cell proportion estimation in minfi and similar packages. The FlowSorted.Blood.EPIC object is based in samples assayed by Brock Christensen and colleagues; for details see Salas et al. 2018. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE110554.
	"""
	
	homepage = "https://github.com/immunomethylomics/FlowSorted.Blood.EPIC"
	bioc = "FlowSorted.Blood.EPIC" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FlowSorted.Blood.EPIC_2.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FlowSorted.Blood.EPIC/FlowSorted.Blood.EPIC_2.6.0.tar.gz"]

	version("2.6.0", sha256="09d1d9b2c8ec3dbdbce673ef29cdea602f6fbf8e7ade39a705c408e0ef0cdd6d")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

