# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcams(RPackage):
	"""In-Depth Characterization and Analysis of Mutational Signatures
('ICAMS')

	Analysis and visualization of experimentally elucidated mutational
    signatures -- the kind of analysis and visualization in Boot et al.,
    "In-depth characterization of the cisplatin mutational signature in 
    human cell lines and in esophageal and liver tumors", Genome Research 2018, 
    <doi:10.1101/gr.230219.117> and
    "Characterization of colibactin-associated mutational signature in an 
    Asian oral squamous cell carcinoma and in other mucosal tumor types",
    Genome Research 2020 <doi:10.1101/gr.255620.119>.
    'ICAMS' stands for In-depth Characterization 
    and Analysis of Mutational Signatures. 'ICAMS' has functions to read in 
    variant call files (VCFs) and to collate the corresponding catalogs of 
    mutational spectra and to analyze and plot catalogs of mutational spectra
    and signatures. Handles both "counts-based" and "density-based" (i.e.
    representation as mutations per megabase) mutational spectra or signatures.
	"""
	
	homepage = "https://github.com/steverozen/ICAMS"
	cran = "ICAMS" 

	version("2.3.12", md5="84dbc97f81dabd74d061f8a8cbfedf72")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
