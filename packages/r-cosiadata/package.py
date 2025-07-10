# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCosiadata(RPackage):
	"""VST normalized RNA-Sequencing data with annotations for multiple species samples from Bgee

	Variance Stabilized Transformation of Read Counts derived from Bgee RNA-Seq Expression Data. Expression Data includes annotations and is across 6 species (Homo sapiens, Mus musculus, Rattus norvegicus, Danio rerio, Drosophila melanogaster, and Caenorhabditis elegans) and across more than 132 tissues. The data is represented as a RData files and is available in ExperimentHub.
	"""
	
	bioc = "CoSIAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/CoSIAdata_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/CoSIAdata/CoSIAdata_1.2.0.tar.gz"]

	version("1.2.0", sha256="3929775871668e252c863d10964a6452be64ffcf03a6fe5d8fa0856cec26a41f")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-experimenthub@2.6:", type=("build", "run"))

