# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlanttfhunter(RPackage):
	"""Identification and classification of plant transcription factors

	planttfhunter is used to identify plant transcription factors (TFs) from protein sequence data and classify them into families and subfamilies using the classification scheme implemented in PlantTFDB. TFs are identified using pre-built hidden Markov model profiles for DNA-binding domains. Then, auxiliary and forbidden domains are used with DNA-binding domains to classify TFs into families and subfamilies (when applicable). Currently, TFs can be classified in 58 different TF families/subfamilies.
	"""
	
	homepage = "https://github.com/almeidasilvaf/planttfhunter"
	bioc = "planttfhunter" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/planttfhunter_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/planttfhunter/planttfhunter_1.2.0.tar.gz"]

	version("1.2.0", md5="94bf35ef27114ae40bdd4be243dfb8fe")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("hmmer", type=("build", "link", "run"))
