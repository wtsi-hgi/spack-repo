# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowsortedCordbloodcombined450k(RPackage):
	"""Illumina 450k/EPIC data on FACS and MACS umbilical blood cells

	Raw data objects to be used for umbilical cord blood cell proportion estimation in minfi and similar packages. The FlowSorted.CordBloodCombined.450k object is based in samples assayed by Bakulski et al, Gervin et al., de Goede et al., and Lin et al.
	"""
	
	homepage = "https://github.com/immunomethylomics/FlowSorted.CordBloodCombined.450k"
	bioc = "FlowSorted.CordBloodCombined.450k" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/FlowSorted.CordBloodCombined.450k_1.18.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/FlowSorted.CordBloodCombined.450k/FlowSorted.CordBloodCombined.450k_1.18.0.tar.gz"]

	version("1.18.0", sha256="146a872d02789fb45da741e9da735c6f8d07b7c03fb840d50933b6a5206f803e")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-minfi@1.21.2:", type=("build", "run"))
	depends_on("r-experimenthub@1.9.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-illuminahumanmethylation450kanno-ilmn12-hg19@0.2.1:", type=("build", "run"))
	depends_on("r-illuminahumanmethylationepicanno-ilm10b4-hg19", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

