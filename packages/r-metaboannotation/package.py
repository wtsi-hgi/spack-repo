# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaboannotation(RPackage):
	"""Utilities for Annotation of Metabolomics Data

	High level functions to assist in annotation of (metabolomics) data sets. These include functions to perform simple tentative annotations based on mass matching but also functions to consider m/z and retention times for annotation of LC-MS features given that respective reference values are available. In addition, the function provides high-level functions to simplify matching of LC-MS/MS spectra against spectral libraries and objects and functionality to represent and manage such matched data.
	"""
	
	homepage = "https://github.com/RforMassSpectrometry/MetaboAnnotation"
	bioc = "MetaboAnnotation" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MetaboAnnotation_1.6.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MetaboAnnotation/MetaboAnnotation_1.6.1.tar.gz"]

	version("1.6.1", md5="fee181fc1795a1e2bde1d1e551f1a45e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-mscoreutils", type=("build", "run"))
	depends_on("r-metabocoreutils", type=("build", "run"))
	depends_on("r-protgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-spectra@1.11.10:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-qfeatures", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-compounddb", type=("build", "run"))
