# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJatsdecoder(RPackage):
	"""A Metadata and Text Extraction and Manipulation Tool Set

	Provides a function collection to extract metadata, sectioned text and study characteristics from scientific articles in 'NISO-JATS' format. Articles in PDF format can be converted to 'NISO-JATS' with the 'Content ExtRactor and MINEr' ('CERMINE', <https://github.com/CeON/CERMINE>). For convenience, two functions bundle the extraction heuristics: JATSdecoder() converts 'NISO-JATS'-tagged XML files to a structured list with elements title, author, journal, history, 'DOI', abstract, sectioned text and reference list. study.character() extracts multiple study characteristics like number of included studies, statistical methods used, alpha error, power, statistical results, correction method for multiple testing, software used. An estimation of the involved sample size is performed based on reports within the abstract and the reported degrees of freedom within statistical results. In addition, the package contains some useful functions to process text (text2sentences(), text2num(), ngram(), strsplit2(), grep2()). See Böschen, I. (2021) <doi:10.1007/s11192-021-04162-z> Böschen, I. (2021) <doi:10.1038/s41598-021-98782-3> and Böschen, I (2023) <doi:10.1038/s41598-022-27085-y>.
	"""
	
	homepage = "https://github.com/ingmarboeschen/JATSdecoder"
	cran = "JATSdecoder" 

	version("1.2.0", md5="62119c6a16a2aed811bb743de420372c")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-opennlp", type=("build", "run"))
