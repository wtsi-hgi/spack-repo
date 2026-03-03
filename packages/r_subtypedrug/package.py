# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubtypedrug(RPackage):
	"""Prioritization of Candidate Cancer Subtype Specific Drugs

	A systematic biology tool was developed to prioritize cancer subtype-specific drugs by integrating genetic perturbation, drug action, biological pathway, and cancer subtype. 
    The capabilities of this tool include inferring patient-specific subpathway activity profiles in the context of gene expression profiles with subtype labels, calculating differentially 
    expressed subpathways based on cultured human cells treated with drugs in the 'cMap' (connectivity map) database, prioritizing cancer subtype specific drugs according to drug-disease 
    reverse association score based on subpathway, and visualization of results (Castelo (2013) <doi:10.1186/1471-2105-14-7>; Han et al (2019) <doi:10.1093/bioinformatics/btz894>; Lamb and Justin (2006) <doi:10.1126/science.1132939>). Please cite using <doi:10.1093/bioinformatics/btab011>.
	"""
	
	cran = "SubtypeDrug" 

	version("0.1.8", md5="b55cbd8fac617545f5879d6ea161f992")
	version("0.1.7", md5="fded9da9e20fbaf4ac6c61a5e785cd9c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-gsva", type=("build", "run"))
	depends_on("r-igraph", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-chemminer", type=("build", "run"))
