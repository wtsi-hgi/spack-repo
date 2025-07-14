# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapredictdsc(RPackage):
	"""Phenotype prediction using microarray data: approach of the best overall team in the IMPROVER Diagnostic Signature Challenge

	This package implements the classification pipeline of the best overall team (Team221) in the IMPROVER Diagnostic Signature Challenge. Additional functionality is added to compare 27 combinations of data preprocessing, feature selection and classifier types.
	"""
	
	homepage = "http://bioinformaticsprb.med.wayne.edu/maPredictDSC"
	bioc = "maPredictDSC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/maPredictDSC_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/maPredictDSC/maPredictDSC_1.40.0.tar.gz"]

	version("1.46.0", tag="RELEASE_3_21")
	version("1.40.0", sha256="c5d1bb45803e681f0c5c34b326f2b71fc08645be0960431edbdade2687ab3725")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-affy", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-gcrma", type=("build", "run"))
	depends_on("r-roc", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-hgu133plus2-db", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-lungcanceracvssccgeo", type=("build", "run"))
