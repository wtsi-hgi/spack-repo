# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClinspacy(RPackage):
	"""Clinical Natural Language Processing using 'spaCy', 'scispaCy',
and 'medspaCy'

	Performs biomedical named entity recognition,
    Unified Medical Language System (UMLS) concept mapping, and negation
    detection using the Python 'spaCy', 'scispaCy', and 'medspaCy' packages, and 
    transforms extracted data into a wide format for inclusion in machine
    learning models. The development of the 'scispaCy' package is described by
    Neumann (2019) <doi:10.18653/v1/W19-5034>. The 'medspacy' package uses
    'ConText', an algorithm for determining the context of clinical statements
    described by Harkema (2009) <doi:10.1016/j.jbi.2009.05.002>. Clinspacy
    also supports entity embeddings from 'scispaCy' and UMLS 'cui2vec' concept
    embeddings developed by Beam (2018) <arXiv:1804.01486>.
	"""
	
	homepage = "https://github.com/ML4LHS/clinspacy"
	cran = "clinspacy" 

	version("1.0.2", md5="1d132b62893312bf1b0a5f7558de9509")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-reticulate@1.16:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-rappdirs", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
