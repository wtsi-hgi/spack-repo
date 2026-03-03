# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneset(RPackage):
	"""Get Gene Sets for Gene Enrichment Analysis

	Gene sets are fundamental for gene enrichment analysis. The package 'geneset' enables querying 
    gene sets from public databases including 'GO' (Gene Ontology Consortium. (2004) <doi:10.1093/nar/gkh036>), 
    'KEGG' (Minoru et al. (2000) <doi:10.1093/nar/28.1.27>), 
    'WikiPathway' (Marvin et al. (2020) <doi:10.1093/nar/gkaa1024>), 
    'MsigDb' (Arthur et al. (2015) <doi:10.1016/j.cels.2015.12.004>), 
    'Reactome' (David et al. (2011) <doi:10.1093/nar/gkq1018>),
    'MeSH' (Ish et al. (2014) <doi:10.4103/0019-5413.139827>), 
    'DisGeNET' (Janet et al. (2017) <doi:10.1093/nar/gkw943>),
    'Disease Ontology' (Lynn et al. (2011) <doi:10.1093/nar/gkr972>), 
    'Network of Cancer Genes' (Dimitra et al. (2019) <doi:10.1186/s13059-018-1612-0>) and 
    'COVID-19' (Maxim et al. (2020) <doi:10.21203/rs.3.rs-28582/v1>).
    Gene sets are stored in the list object which provides data frame of 'geneset' and 'geneset_name'. 
    The 'geneset' has two columns of term ID and gene ID. The 'geneset_name' has two columns of 
    terms ID and term description.
	"""
	
	homepage = "https://github.com/GangLiLab/geneset"
	cran = "geneset" 

	version("0.2.7", md5="7388d1a6504a3396f4bc15112b197c7c")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-fst", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
